#Required input fields to list a bike on Craigslist

_wheelSize = {'10 in':'1','12 in':'2','14 in':'3','16 in':'4','18 in':'5','20 in':'6','24 in':'7','26 in':'8','27 in':'9','28 in':'10','29 in':'11','650B':'12','650C':'13','700C':'14','other/unknown':'15'}
_frameMaterial = {'alloy':'1','aluminum':'2','carbon fiber':'3','composite':'4','scandium':'5','steel':'6','titanium':'7','other/unknown':'8'}
_bicycleType = {'bmx':'1','cargo/pedicab':'2','cruiser':'3','cyclocross':'4','folding':'5','hybrid/comfort':'6','kids':'7','mountain':'8','recumbent/trike':'9','road':'10','tandem':'11','track':'12','other/unknown':'13'}
_suspension = {'suspension fork (hardtail)':'1','frame and fork':'2','no suspension (rigid)':'3','other/unknown':'4'}
_brakeType = {'Caliper':'1', 'Cantilever':'2', 'Coaster':'3', 'Disc (hydraulic)':'4', 'Disc (Mechanical)':'5', 'Drum':'6', 'Gyro / Bmx':'7','Hydro Rim Brakes':'8', 'none':'9','V Brakes':'10', 'U Brakes':'11', 'Unknown/Other':'12'}
_handlebarType = {'Aero':'1', 'bmx':'2', 'Bullhorn':'3', 'Cruiser':'4', 'Drop':'5', 'Flat':'6', 'Riser':'7', 'Triathlon':'8', 'Other/Unknown':'9'}
_electricAssist = {'None':'1', 'Pedal Assist':'2', 'Throttle':'3', 'Other':'4'}
_condition = {'New - Dealer/Store':'10', 'Excellent':'20', 'Excellent':'30', 'Good':'40', 'Pair':'50', 'For parts / not working':'60', 'other':'70'}





postData = {
    'userID': '1',
    'title': 'Bike for sale',
    'price': '100',
    'year': '2018',
    'make': 'Giant',
    'model': 'Talon',
    'bikeType': 'bmx',
    'frameMaterial': 'aluminum',
    'frameSize': 'Medium',
    'suspension':'suspension fork (hardtail)',
    'brakeType': 'disc (mechanical)',
    'handlebarType': 'flat',
    'electricAssist': 'none',
    'wheelSize': '26 in',
    'description':'This is a bike for sale',
    'serialNum':'1234567890',
    'condition': 'like new',


}











bikeCraigslist = {
    'userID':postData['userID'],
    
    'edit':
        {
            "PostingTitle":postData['title'],
            "price":postData['price'],
            "geographic_area":"North Van",
            "postal":"V7N3J6",
            "PostingBody":postData['description'],
            "bicyle_frame_size_freeform":postData['frameSize'],
            "sale_manufacturer":postData['make'],
            "sale_model":postData['model'],
            "serial_number":postData['serialNum'],
            "bicycle_type":_bicycleType[postData['bikeType']],
            "bicycle_wheel_size":_wheelSize[postData['wheelSize']],
            "bicycle_frame_material":_frameMaterial[postData['frameMaterial']],
            "bicycle_suspension":_suspension[postData['frontSuspension']],
            "bicycle_brake_type":_brakeType[postData],
            "bicycle_handlebar_type":_handlebarType[postData['handlebarType']],
            "bicycle_electric_assist":_electricAssist[postData['electricAssist']],
            "condition":_condition[postData['condition']],
            "language":"5",
            "FromEMail":'bit4104@gmail.com',
            "Privacy":"C",
            "go":"continue"  
        }

}




'''
Sample JSON input to the format class:

{
    'userID': '1',
    'title': 'Bike for sale',
    'price': '100',
    'year': '2018',
    'make': 'Giant',
    'model': 'Talon',
    'bikeType': 'bmx',
    'frameMaterial': 'aluminum',
    'frameSize': 'Medium',
    'frontSuspension':'suspension fork (hardtail)',
    'brakeType': 'disc (mechanical)',
    'handlebarType': 'flat',
    'electricAssist': 'none',
    'wheelSize': '26 in',
    'condition': 'like new',

}

Converted
bikeType: bmx -> 1
frameMaterial: aluminum -> 2
'''


'''
Sample JSON output from the format class for Craigslist:
    'email': 'bob@example.com',
    'password': 'Bike for sale',
    'price': '100',
    'year': '2018',
    'make': 'Giant',
    'model': 'Talon',
    'bikeType': '1',
    'frameMaterial': '2',
    'frameSize': 'Medium',
    'frontSuspension':'1',
    'brakeType': '5',
    'handlebarType': '6',
    'electricAssist': 'none',
    'wheelSize': '26 in',
    'condition': 'like new',
'''


