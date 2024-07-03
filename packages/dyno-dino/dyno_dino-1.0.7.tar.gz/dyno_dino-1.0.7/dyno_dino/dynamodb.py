import logging
import base64
from typing import Any, Dict, List


def _is_string_set(value: List[Any]) -> bool:
    return all(isinstance(i, str) for i in value)


def _is_number_set(value: List[Any]) -> bool:
    return all(isinstance(i, (int, float)) for i in value)


def _is_binary_set(value: List[Any]) -> bool:
    try:
        for i in value:
            if isinstance(i, bytes):
                base64.b64decode(i, validate=True)
            elif isinstance(i, str):
                base64.b64decode(i.encode('utf-8'), validate=True)
            else:
                return False
        return True
    except (base64.binascii.Error, ValueError, TypeError):
        return False


def _is_base64(s: str) -> bool:
    try:
        if isinstance(s, str):
            if base64.b64encode(base64.b64decode(s.encode('utf-8'))).decode('utf-8') == s:
                return True
        return False
    except Exception:
        return False


def _convert_to_dynamodb(data: Any) -> Dict[str, Any]:
    dynamodb_data = {}
    if isinstance(data, dict):
        for key, value in data.items():
            dynamodb_data[key] = _convert_value(value)
    else:
        dynamodb_data = _convert_value(data)
    return dynamodb_data


def _convert_value(value: Any) -> Dict[str, Any]:
    if isinstance(value, str):
        if _is_base64(value):
            return {'B': value}
        else:
            return {'S': value}
    elif isinstance(value, bool):
        return {'BOOL': value}
    elif isinstance(value, int) or isinstance(value, float):
        return {'N': str(value)}
    elif value is None:
        return {'NULL': True}
    elif isinstance(value, bytes):
        return {'B': base64.b64encode(value).decode('utf-8')}
    elif isinstance(value, dict):
        return {'M': _convert_to_dynamodb(value)}
    elif isinstance(value, list):
        if _is_string_set(value):
            return {'SS': value}
        elif _is_number_set(value):
            return {'NS': [str(i) for i in value]}
        elif _is_binary_set(value):
            return {'BS': [base64.b64encode(i).decode('utf-8') if isinstance(i, bytes) else i for i in value]}
        else:
            list_items = []
            for item in value:
                list_items.append(_convert_value(item))
            return {'L': list_items}
    else:
        logging.error(f"Unsupported type for DynamoDB: {type(value)}")
        return {}


def _convert_from_dynamodb(dynamodb_data: Dict[str, Any]) -> Any:
    if 'S' in dynamodb_data:
        return dynamodb_data['S']
    elif 'N' in dynamodb_data:
        return float(dynamodb_data['N']) if '.' in dynamodb_data['N'] else int(dynamodb_data['N'])
    elif 'B' in dynamodb_data:
        return base64.b64encode(base64.b64decode(dynamodb_data['B'])).decode('utf-8')
    elif 'BOOL' in dynamodb_data:
        return dynamodb_data['BOOL']
    elif 'NULL' in dynamodb_data:
        return None
    elif 'M' in dynamodb_data:
        return {k: _convert_from_dynamodb(v) for k, v in dynamodb_data['M'].items()}
    elif 'L' in dynamodb_data:
        return [_convert_from_dynamodb(v) for v in dynamodb_data['L']]
    elif 'SS' in dynamodb_data:
        return dynamodb_data['SS']
    elif 'NS' in dynamodb_data:
        return [float(n) if '.' in n else int(n) for n in dynamodb_data['NS']]
    elif 'BS' in dynamodb_data:
        return [base64.b64encode(base64.b64decode(b)).decode('utf-8') for b in dynamodb_data['BS']]
    else:
        raise ValueError(f"Unsupported DynamoDB type: {dynamodb_data}")


def convert_dynamodb_to_json(dynamodb_data: dict):
    if not isinstance(dynamodb_data, dict) or 'M' not in dynamodb_data:
        dynamodb_data = {'M': dynamodb_data}
    json_data = _convert_from_dynamodb(dynamodb_data)
    return json_data


def convert_json_to_dynamodb(data: dict):
    dynamodb_json = _convert_to_dynamodb(data)
    return dynamodb_json