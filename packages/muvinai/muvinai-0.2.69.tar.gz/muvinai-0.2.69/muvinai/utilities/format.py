import json
import typing
from datetime import date, datetime

import iso8601
from bson import ObjectId

from .dates import localize


def is_jsonable(x):
    try:
        json.dumps(x)
        return True
    except (TypeError, OverflowError):
        return False


def datetime_parser(obj: typing.Union[dict, list, str]) -> typing.Union[dict, list, str]:
    """ Parsear las fechas de un diccionario a formato iso 8601

    :param obj: Diccionario, lista o string a parsear
    :type obj: Diccionario, lista o string
    :return: Diccionario, lista o string parseado
    :rtype: Diccionario, lista o string
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, dict) or isinstance(v, list):
                obj[k] = datetime_parser(v)
            if isinstance(v, str) and len(v) > 9:
                try:
                    obj[k] = iso8601.parse_date(v)
                except:
                    pass
            if isinstance(v, str) and len(v) == 24:
                try:
                    obj[k] = ObjectId(v)
                except:
                    pass
    if isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, dict) or isinstance(v, list):
                obj[i] = datetime_parser(v)
            if isinstance(v, str) and len(v) > 9:
                try:
                    obj[i] = iso8601.parse_date(v)
                except:
                    pass
            if isinstance(v, str) and len(v) == 24:
                try:
                    obj[i] = ObjectId(v)
                except:
                    pass
    return obj


def json_serial(dct: dict) -> dict:
    for k, v in dct.items():
        if isinstance(v, dict):
            dct[k] = json_serial(v)
        elif isinstance(v, (datetime, date)):
            dct[k] = localize(v).isoformat()
        elif isinstance(v, list):
            dct[k] = list_to_json(v)
        elif is_jsonable(v):
            dct[k] = v
        else:
            dct[k] = str(v)
    return dct


def list_to_json(data: list) -> list:
    result = list()
    for e in data:
        if isinstance(e, dict):
            result.append(json_serial(e))
        elif isinstance(e, list):
            result.append(list_to_json(e))
        elif isinstance(e, (datetime, date)):
            result.append(localize(e).isoformat())
        elif is_jsonable(e):
            result.append(e)
        else:
            result.append(str(e))
    return result


def format_ids(dct: dict) -> dict:
    """ Cambiar las claves de diccionario "_id" a "id"

    :param dct: diccionario con claves "_id"
    :type dct: dict
    :return: Diccionario modificado
    :rtype: dict
    """
    return {"id": dct.pop("_id", None), **dct}


def format_object_ids(dct: dict) -> dict:
    """ Crear un diccionario igual al que se recibe por parametro pero las \
        claves "id" se actualizan a "_id" y los valores de estas claves se \
        convierten a ObjectId

    :param dct: diccionario original
    :type dct: dict
    :return: diccionario actualizado
    :rtype: dict
    """
    return {"_id": ObjectId(dct.pop("id", None)), **dct}


def muvi_print(color_message: str, message: str) -> str:
    """ Colores para mensajes
    :param color_message: puede ser error, warning, info, successful
    :type color_message: str
    :param message: variable a printear
    :type message: any
    """
    color_message = color_message.lower()

    color_dict = {
        "error": "\x1b[0;30;41m",
        "warning": "\x1b[0;37;43m",
        "info": "\x1b[0;30;44m",
        "successful": "\x1b[0;30;42m",
        "head": "\x1b[0;30;45m",
        "normal": "\x1b[0m"
    }

    default_color = color_dict.get("normal")

    color = color_dict.get(color_message, default_color)

    print(color, message, default_color)
