from django.shortcuts import redirect, render,HttpResponse
from . models import Role, Location , User, ServiceCategory, Worker

# Create your views here.
def first(request):
    return HttpResponse("avinash")


def signup(request):
    return render(request,"signup.html")    

def login(request):
    if request.GET:
        email = request.GET["email"]
        password = request.GET["password"]
        role= request.GET["role"]
        try:
            user = User.objects.filter(email=email, password=password, role_id_id=role) 
            print(len(user))
            if len(user) == 1:
                request.session["email"] = email
                data=ServiceCategory.objects.all()
                location= Location.objects.all()
                return render(request, "dashboard.html", {"user": request.session["email"], "data": data , "location": location})
            else:
                return HttpResponse("invalid login")
        except:
            return HttpResponse("invalid login do signup")  
    return render(request,"login.html")

def service(request):
    return render(request,"service.html") 



def user(request):
    if request.GET:
        name=request.GET["name"]
        email=request.GET["email"]
        address=request.GET["address"]
        mobile= request.GET['mobile']
        password=request.GET['password']
        role = request.GET['role']
        print(name,email,address,mobile,password,role)
        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already exists")
        else:
            User(name=name, email=email, role_id_id=role,  mobile=mobile, password=password, location_id=address).save()

    return render(request, "user.html")

def main(request):
    if request.GET:
        email =  request.session.get("email")
        print(email)
        location = request.GET["location"]
        category= request.GET["category"]
        data1= Worker.objects.filter(location_id=location, category_id_id=category)
    return render(request,"dashboard.html",{"user": email, "data1":data1})

def logout(request):
    # try:
    #     del request.session["email"]
    # except KeyError:
    #     pass
    return HttpResponse("You have been logged out successfully")  # Redirect to a logout success page or home page
