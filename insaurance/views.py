from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
import json
from django.db.models import Q, F, ExpressionWrapper, DateField
from datetime import timedelta


# Create your views here.
@api_view(['GET'])
def get_Category(request):

    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['GET'])
def get_Products(request):

    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['POST'])
def create_Lead(request):
    data = request.data

    print(data)

    lead = Lead.objects.create(
        customer_name=request.data['customer_name'],
        mobile_number=request.data['mobile_number'],
        email=request.data['email'],
        model=request.data['model'],
        engine_number=request.data['engine_number'],
        chassis_number=request.data['chassis_number'],

        nominee_name=request.data['nominee_name'],
        nominee_age=request.data['nominee_age'],
        nominee_relation=request.data['nominee_relation'],
        hypothecation=request.data['hypothecation'],
        invoice_image=request.data['invoiceimage'],
        otherkyc_image=request.data['otherkycimage'],
        aadharcardf_image=request.data['afimage'],
        aadharcardb_image=request.data['abimage'],
        pan_image=request.data['panimage'],
        price=float(request.data['price']),

        product=Product.objects.get(id=request.data['selectproduct'])

    )

    lead.save()

    return Response({
        "status": 201,
        "msg": 'generated'
    })


@api_view(['PATCH'])
def update_lead(request, pk):

    data = request.data

    print('data', data)

    print(request.data['customer_name'])

    lead = Lead.objects.get(id=pk)

    print('lead1', lead)
    print(type(request.data['customer_name']))
    print('mobile', request.data['mobile_number'])
    # print(type(lead.customer_name))

    lead.customer_name = request.data['customer_name']

    lead.mobile_number = request.data['mobile_number']
    # lead.email = request.data['email'],
    # lead.model = request.data['model'],
    # lead.engine_number = request.data['engine_number'],
    # lead.chassis_number = request.data['chassis_number'],

    # lead.nominee_name = request.data['nominee_name'],
    # lead.nominee_age = request.data['nominee_age'],
    # lead.nominee_relation = request.data['nominee_relation'],
    # lead.hypothecation = request.data['hypothecation'],
   # lead.image = request.data['image'],
    #lead.price = float(request.data['price']),

    lead.save()

    return Response({
        "status": 201,
        "msg": "updated"
    })


@api_view(['GET'])
def get_Leads(request):

    leads = Lead.objects.all()

    print('all leads', leads)
    serializer = LeadSerializer(leads, many=True)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['GET'])
def get_Lead(request, pk):

    leads = Lead.objects.get(id=pk)

    print('leds', leads)
    serializer = LeadSerializer(leads, many=False)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['POST'])
def create_Request(request):
    data = request.data

    usermappingrequest = UserMappingRequest.objects.create(
        customer_name=request.data['customer_name'],
        registration_number=int(request.data['registration_number']),
        insurer_name=request.data['insurer_name'],

        policy_number=int(request.data['policy_number']),
        premium=float(request.data['premium']),
        image=request.data['image'],

        product=Product.objects.get(id=request.data['selectproduct'])


    )

    usermappingrequest.save()

    return Response({
        "status": 201,
        "msg": 'generated'
    })


@api_view(['GET'])
def get_UserGeneratedRequests(request):

    userrequests = UserMappingRequest.objects.annotate(
        renewal_at=ExpressionWrapper(F('created_at') + timedelta(days=365), output_field=DateField()))
    serializer = UserMappingRequestSerializer(userrequests, many=True)

    return Response({
        "status": 200,
        "data": serializer.data,
        "msg": "get data"
    })


@api_view(['GET'])
def get_UserGeneratedRequest(request, pk):

    userrequests = UserMappingRequest.objects.get(id=pk)
    serializer = UserMappingRequestSerializer(userrequests, many=False)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['PUT'])
def update_UserGeneratedRequest(request, pk):

    renew = UserMappingRequest.objects.get(id=pk)

    renew.customer_name = request.data['customer_name']
    renew.registration_number = request.data['registration_number']
    renew.insurer_name = request.data['insurer_name']
    renew.policy_number = request.data['policy_number']
    renew.premium = request.data['premium']

    renew.image = request.data['image']

    renew.status = request.data['status']

    renew.save()

    serializer = UserMappingRequestSerializer(renew, many=False)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['GET'])
def get_UserResolvedRequests(request):

    userrequests = UserMappingRequest.objects.filter(status='Resolved')
    serializer = UserMappingRequestSerializer(userrequests, many=True)

    return Response({
        "status": 200,
        "data": serializer.data
    })

# Create Ticket for Request


@api_view(['POST'])
def create_Ticket(request):
    data = request.data

    issues = json.loads(request.data['issue'])

    request_id = request.data['request_Id']
    print(request_id)

    myrequest = UserMappingRequest.objects.get(id=request_id)

    # myrequest2 = UserMappingRequest.objects.get(id=request_id)
    print("my", myrequest)

    # myrequest_json = UserMappingRequestSerializer(myrequest, many=False)

    # print("data", myrequest_json.data["id"])

    # mylead = Lead.objects.filter(id=request_id).first()

    # lead_json = LeadSerializer(mylead, many=False)

    # print("lead_id", lead_json.data, "exist")

    # print("mylead", mylead)

    # print("myrequest", type(myrequest))

    issues_list = []

    for i in range(len(issues)):

        ticket = Ticket(
            issue=issues[i],
            myrequest=UserMappingRequest.objects.get(id=request_id),
            # mylead=Lead.objects.get(id=request_id)

        )

        issues_list.append(ticket)

    # if not mylead:

    #     for i in range(len(issues)):

    #         ticket = Ticket(
    #             issue=issues[i],
    #             myrequest=UserMappingRequest.objects.get(id=request_id),
    #             # mylead=Lead.objects.get(id=request_id)

    #         )

    #     issues_list.append(ticket)

    Ticket.objects.bulk_create(issues_list)

    print(data)

    return Response({
        "status": 201,
        # "myreuest":  ,
        # "mylead": json.dumps(mylead)
    })


@api_view(['GET'])
def get_Issues(request, Id):

    issues = Ticket.objects.filter(Q(myrequest__id=Id) | Q(mylead__id=Id))

    print(issues)

    serializer = TicketSerializer(issues, many=True)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['PATCH'])
def update_ticket(request, pk):

    data = request.data

    print(data)

    issue = Ticket.objects.get(id=pk)

    print(issue)

    issue.old_value = request.data['oldvalue']
    issue.new_value = request.data['newvalue']

    issue.save()

    return Response({
        "status": "201"
    })


# Create Ticket For Lead


@api_view(['POST'])
def createlead_Ticket(request):
    data = request.data

    issues = json.loads(request.data['issue'])

    request_id = request.data['request_Id']
    print(request_id)

    # myrequest = UserMappingRequest.objects.filter(id=request_id).first()

    # myrequest2 = UserMappingRequest.objects.get(id=request_id)
    # print("my", myrequest2)

    # myrequest_json = UserMappingRequestSerializer(myrequest, many=False)

    # print("data", myrequest_json.data["id"])

    mylead = Lead.objects.filter(id=request_id).first()

    # lead_json = LeadSerializer(mylead, many=False)

    # print("lead_id", lead_json.data, "exist")

    # print("mylead", mylead)

    # print("myrequest", type(myrequest))

    issues_list = []

    for i in range(len(issues)):

        ticket = Ticket(
            issue=issues[i],

            mylead=Lead.objects.get(id=request_id)

        )

        issues_list.append(ticket)

    LeadTicket.objects.bulk_create(issues_list)

    print(data)

    return Response({
        "status": 201,

    })


@api_view(['GET'])
def getlead_Issues(request, Id):

    issues = LeadTicket.objects.filter(Q(mylead__id=Id))

    print(issues)

    serializer = TicketSerializer(issues, many=True)

    return Response({
        "status": 200,
        "data": serializer.data
    })


@api_view(['PATCH'])
def updatelead_ticket(request, pk):

    data = request.data

    print(data)

    issue = LeadTicket.objects.get(id=pk)

    print(issue)

    issue.old_value = request.data['oldvalue']
    issue.new_value = request.data['newvalue']

    issue.save()

    return Response({
        "status": "201"
    })
