# -*- coding: utf-8 -*-
from ..component import Component

from .models import Style


@Component.registry.register
class MapserverStyleComponent(object):
    pass