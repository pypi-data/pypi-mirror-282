from typing import Any, Optional, Set, Callable, Iterator
from collections.abc import Mapping, Iterable
import uuid

from specklepy.objects import Base, units
from specklepy.objects.other import Collection
from specklepy.api import operations
from specklepy.api.wrapper import StreamWrapper

import pandas as pd

import lcax.pydantic as lcax

import json

import logging

######################## CLASSES ##########################

class Product(Base, 
              speckle_type ="Product",
              detachable={"epdx"}):

    def __setattr__(self, key, value):
        self[key] = value
        super().__setattr__(key, value)

    def __delattr__(self, key):
        del self[key]
        super().__delattr__(key)

#    def __getattr__(self, key):
#        return self[key]

    def __init__(self, **kwargs):
        """ properties:
        self.__delattr__("name")
        self.__delattr__("epd_id")
        self.__delattr__("source_name") 
        self.__delattr__("source_url")
        self.__delattr__("declared_unit")
        self.__delattr__("version")
        self.__delattr__("published_date")
        self.__delattr__("valid_until")
        self.__delattr__("standard")
        self.__delattr__("location")
        self.__delattr__("linear_density")
        self.__delattr__("bulk_density") 
        self.__delattr__("gross_density")
        self.__delattr__("grammage")
        self.__delattr__("layer_thickness")
        self.__delattr__("subtype")
        self.__delattr__("epdx") """

        self.__dict__.update(**kwargs)

    @classmethod
    def fromDict(cls, dict):
        """
        to be used with rows from a dataframe, using for instance df.to_dict(orient="records")
        """
        product = cls()
        for key in dict.keys():
            setattr(product, key, dict[key])

        return product
    
    @classmethod
    def fromEpdx(cls, epdx : json):

        product = cls()

        def find_conversion(_epdx, metadata):
            conversions = _epdx['conversions']
#        print("type of conversions is {0}".format(type(conversions)))
            if conversions == None:
                return 0
            for conversion in conversions:
                conv_metadata = json.loads(conversion["meta_data"])
#            print("type of conversions metadata is {0}".format(type(conv_metadata)))            
                if conv_metadata["name"] == metadata:
                    return float(conv_metadata["value"])
            return 0

        product.epdx = epdx
        epdx_dict = json.loads(epdx)
        product.linear_density = 0
        product.gross_density = 0
        product.grammage = 0
        product.layer_thickness = 0
        product.bulk_density = 0
        product.impact_category = []

        for key, value in epdx_dict.items():
            if key == "conversions":
                product.linear_density = find_conversion(epdx_dict, "linear density")
                product.gross_density = find_conversion(epdx_dict, "gross density")
                product.grammage = find_conversion(epdx_dict, "grammage")
                product.layer_thickness = find_conversion(epdx_dict, "layer thickness")
                product.bulk_density = find_conversion(epdx_dict, "bulk thickness")
            elif key in lcax.ImpactCategoryKey._value2member_map_:
                product.impact_category.append({key: value})
            else:
                setattr(product, key, value)
        return product
    


class Part(Collection,
           speckle_type = "Part"):
    id = str
    name = str
    part_quantity = float
    part_unit = str
    epd_source = dict
    epd_id = str

    def __init__(self, epd_source : Product = None):
        self.id = uuid.uuid4      # should generate the guid by serialising other parameters
        self.part_quantity = 0
        self.mapping_name = ""
        self.mapping = ""
        if epd_source is not None:
            self.name = epd_source["name"]
            self.part_unit = epd_source["declared_unit"]
            self.epd_source = {"EPD" : json.loads(epd_source["epdx"])}
            self.epd_id = epd_source["id"]

    

class Buildup(Collection,
              speckle_type = "Buildup",
              detachable = {"parts"}):
    def __init__(self):
        pass

    id = str
    name = str
    description = str
    classification = list
    parts = dict
    quantity = float
    unit = str