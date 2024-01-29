from datetime import datetime

from pydantic import BaseModel


class Comments(BaseModel):

    text : str
    photo : bytes
    date : datetime
    mark : float
    product_id : int
    user_id : int


