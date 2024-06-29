# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  ctrip-helper
# FileName:     flight_desktop_ui.py
# Description:  TODO
# Author:       GIGABYTE
# CreateDate:   2024/06/26
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import gzip
from enum import Enum
from json import loads
from decimal import Decimal
from selenium import webdriver
from ctrip_helper.config import url_map
from ctrip_helper.utils import get_current_ct
from ctrip_helper.libs import logger, get_element


class UILocatorRegx(Enum):
    flight_list_filter_header = {"locator": "xpath", "regx": '//ul[@class="filterbar-v2"]'}


class SeleniumApi(object):

    @classmethod
    def get_url(cls, suffix: str) -> str:
        return "{}://{}{}".format(url_map.get("protocol"), url_map.get("domain"), suffix or "")

    @classmethod
    def open_search_flight_list_page(cls, driver: webdriver, departure_city_code: str, departure_date: str,
                                     arrival_city_code: str, loop: int = 1, sleep: float = 0.0, **kwargs) -> bool:
        url_suffix = url_map.get('h2_flight_list').format(departure_city_code, arrival_city_code)
        dept_date = departure_date[:10] if len(departure_date) > 10 else departure_date
        ct = get_current_ct()
        url_suffix = url_suffix + "?_=1&depdate={}&sortByPrice=true&cabin=Y_S_C_F&ct={}".format(dept_date, ct)
        driver.get(cls.get_url(suffix=url_suffix))
        flight_list_filter_header_element = get_element(
            driver=driver, locator=UILocatorRegx.flight_list_filter_header.value.get("locator"),
            regx=UILocatorRegx.flight_list_filter_header.value.get("regx"), loop=loop, sleep=sleep, **kwargs
        )
        logger.info("打开国内机票航班查询页")
        if flight_list_filter_header_element:
            return True
        else:
            return False

    @classmethod
    def get_airline_flight_list_with_request(cls, driver: webdriver) -> dict:
        data = dict()
        url_prefix = cls.get_url(suffix=url_map.get('flight_list'))
        for request in driver.requests:
            url = request.url
            if url.startswith(url_prefix) is True:
                status_code = request.response.status_code
                if status_code == 200:
                    body = request.response.body
                    if body:
                        if request.response.headers.get("content-encoding") == "gzip":
                            data = loads(gzip.decompress(body).decode("utf-8"))
                        else:
                            data = loads(body.decode("utf-8"))
                break
        return data

    @classmethod
    def parse_flight_data_with_json(cls, data: dict) -> list:
        flight_itinerarys = data.get("data").get("flightItineraryList") or list() if isinstance(
            data.get("data"), dict) else list()
        parse_data = list()
        for flight_itinerary in flight_itinerarys:
            itinerary_id = flight_itinerary.get("itineraryId")
            itinerary_id_slice = itinerary_id.split(",")
            if len(itinerary_id_slice) == 1:
                flight_segment = flight_itinerary.get("flightSegments")[0]
                airline_code = flight_segment.get("airlineCode")
                airline_name = flight_segment.get("airlineName")
                duration = flight_segment.get("duration")
                flight_info = flight_segment.get("flightList")[0]
                flight_no = flight_info.get("flightNo")
                operate_flight_no = flight_info.get("operateFlightNo")
                # 如果有值，说明是共享航班
                if operate_flight_no:
                    continue
                departure_city_code = flight_info.get("departureCityCode")
                arrival_city_code = flight_info.get("arrivalCityCode")
                departure_city_name = flight_info.get("departureCityName")
                arrival_city_name = flight_info.get("arrivalCityName")
                departure_airport_code = flight_info.get("departureAirportCode")
                arrival_airport_code = flight_info.get("arrivalAirportCode")
                departure_airport_name = flight_info.get("departureAirportName")
                arrival_airport_name = flight_info.get("arrivalAirportName")
                departure_terminal = flight_info.get("departureTerminal")
                arrival_terminal = flight_info.get("arrivalTerminal")
                departure_datetime = flight_info.get("departureDateTime")
                arrival_datetime = flight_info.get("arrivalDateTime")
                price_slice = flight_itinerary.get("priceList")
                for price in price_slice:
                    group_type = price.get("groupType")
                    penalty = price.get("penalty") if isinstance(price, dict) else dict()
                    penalty_criteria = loads(penalty.get("penaltyCriteria")) if isinstance(
                        penalty.get("penaltyCriteria"), str
                    ) else dict()
                    price_unit_criteria_list = penalty_criteria.get("priceUnitCriteriaList") if isinstance(
                        penalty_criteria.get("priceUnitCriteriaList"), list
                    ) else list()
                    sub_cabin = [x.get("subClass") for x in price_unit_criteria_list]
                    sub_cabin = "|".join(sub_cabin) if sub_cabin else ""
                    if group_type == "Airline":
                        adult_price = Decimal(str(price.get("adultPrice"))) if price.get("adultPrice") else Decimal(
                            "0.00")
                        child_price = Decimal(str(price.get("childPrice"))) if price.get("childPrice") else Decimal(
                            "0.00"
                        )
                        infant_price = Decimal(str(price.get("infantPrice"))) if price.get("infantPrice") else Decimal(
                            "0.00"
                        )
                        invoice_type = price.get("invoiceType")
                        cabin = price.get("cabin")
                        parse_data.append(dict(
                            flight_no=flight_no, adult_price=str(adult_price), child_price=str(child_price),
                            infant_price=str(infant_price), invoice_type=str(invoice_type), cabin=str(cabin),
                            sub_cabin=sub_cabin, airline_code=airline_code, airline_name=airline_name,
                            duration=duration, departure_city_code=departure_city_code,
                            arrival_city_code=arrival_city_code, departure_city_name=departure_city_name,
                            arrival_city_name=arrival_city_name, departure_airport_code=departure_airport_code,
                            arrival_airport_code=arrival_airport_code, departure_airport_name=departure_airport_name,
                            arrival_airport_name=arrival_airport_name, departure_terminal=departure_terminal,
                            arrival_terminal=arrival_terminal, departure_datetime=departure_datetime,
                            arrival_datetime=arrival_datetime,
                        ))
                        break
        parse_data.sort(key=lambda x: x.get("adult_price"))
        return parse_data
