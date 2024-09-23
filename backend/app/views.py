from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Item
import json

@require_http_methods(["GET"])
def get_items(request):
    items = list(Item.objects.values())
    return JsonResponse(items, safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def create_item(request):
    try:
        data = json.loads(request.body)
        item = Item.objects.create(            
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price')
        )
        item_json = {
            '_id': item._id,
            'name': item.name,
            'description': item.description,
            'price': item.price
        }
        return JsonResponse({'message': 'Item created successfully','record':item_json}, status=201)
    except Exception as e:
        if 'cannot be null' in str(e):
            return JsonResponse({'message': 'Item validation failed'}, status=400)
        else:
            return JsonResponse({'message': 'Error Occured: ' + str(e)}, status=400)
    

@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        data = json.loads(request.body)
        item.name = data.get('name', item.name)
        item.description = data.get('description', item.description)
        item.price = data.get('price', item.price)
        item.save()
        item_json = {
            '_id': item._id,
            'name': item.name,
            'description': item.description,
            'price': item.price
        }
        return JsonResponse({'message': 'Item updated successfully','record':item_json})
    except Exception as e:
        if 'cannot be null' in str(e):
            return JsonResponse({'message': 'Item validation failed'}, status=400)
        else:
            return JsonResponse({'message': 'Error Occured: ' + str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
        item.delete()
        return JsonResponse({'message': 'Item deleted successfully'})
    except Exception as e:
        return JsonResponse({'message': 'Error Occured: ' + str(e)}, status=400)
