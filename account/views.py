from rest_framework import status 
from .models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from account.serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
# Create your views here.

# /account/register/
@api_view(['POST',])
def registration_view(request):
	if request.method == 'POST':  #checking if a valid request of type 'POST'
		serializer = RegistrationSerializer(data=request.data) #intializing the Registration Serializer
		if serializer.is_valid(): #check if the serializer is valid with all required fields
			account = serializer.save() #if valid save the serializer
			token = Token.objects.get(user=account).key
			return Response({'id':account.pk,'first_name':account.first_name,'last_name':account.last_name,'email':account.email},content_type='application/json',status=200)
		else: #if the serializer is not valid return appropriate error
			data = serializer.errors
			return Response({'error':data},content_type='application/json',status=500)

# /account/user_details/
@api_view(['GET',])
def user_details(request):
	user_id = request.query_params['id']  #fetching the user id using query parameters
	try:
		data = User.objects.get(pk = user_id) #fetching user detail with the given user id
		return Response({'id':user_id,'first_name':data.first_name,'last_name':data.last_name,'email':data.email},content_type='application/json',status=200)
	except:
		return Response({'error':'user id not valid'}) #if the details for the user id does not exist return error
		
