import datetime
import os

import django

from Vault.models import Clip

# Will used from Auto generated from personal tool

def insert_db(Title, CreatedAt, ViewCount, LengthInSecond, VideoId):
    c = Clip()
    c.Title = Title
    dt = datetime.datetime.strptime(CreatedAt, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    c.CreatedAt = dt
    c.ViewCount = ViewCount
    c.LengthInSecond = LengthInSecond
    c.VideoId = VideoId
    c.save()