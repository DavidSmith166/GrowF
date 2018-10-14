import json
from rest_framework.renderers import JSONRenderer

class StockJSONRenderer(JSONRenderer):
    charset = 'utf-8'
    def render(self, data, media_type=None, renderer_context=None):
        errors = data.get('errors', None)
        
        if errors is not None:
            return super(StockJSONRenderer, self).render(data)
        return json.dumps({
                'stock': data
            })