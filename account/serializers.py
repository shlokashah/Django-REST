from rest_framework import serializers
from .models import User
class RegistrationSerializer(serializers.ModelSerializer):

	password2 = serializers.CharField(style={'input_type':'password'},write_only=True)

	class Meta:
		model= User
		fields=['first_name','last_name','email','password','password2']
		extra_kwargs={
					'password':{'write_only':True}
		}

	def save(self):
		account = User(first_name=self.validated_data['first_name'],last_name=self.validated_data['last_name'],email=self.validated_data['email'])
		password = self.validated_data['password']
		password2 = self.validated_data['password2']
		# user_type = self.user_type
		if password!=password2:   # check if the two passwords are same
			raise serializers.ValidationError({'password':'Passwords must match'})  # if passwords do not match raise error

		account.set_password(password) 
		account.save()
		return account


