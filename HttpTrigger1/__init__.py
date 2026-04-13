import logging
import azure.functions as func
from .. import model

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('ML Function triggered')

    try:
        value = int(req.params.get('value'))
    except:
        value = 10

    result = model.predict(value)

    return func.HttpResponse(f"Prediction Result: {result}")
