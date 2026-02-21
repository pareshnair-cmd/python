shutdown_option1 = str(input("do you want to shut down? - "))
shutdown_option2 = str(input("did you save your files you need? - "))                   
def shutdown (shutdown_option1,shutdown_option2 = 'yes'):
    return (shutdown)
if shutdown_option1 == 'yes' and shutdown_option2 == 'yes':
    print ("initiating shutdown")
elif shutdown_option1 == 'no' and shutdown_option2 == 'yes':
    print ("make sure if you want to shutdown")
elif shutdown_option1 == 'yes' and shutdown_option2 == 'no':
    print ("please save the files you need")
elif  shutdown_option1 == 'no' and shutdown_option2 == 'no':
    print ("abort shutdown")
elif shutdown_option1 != 'no'or 'yes' and shutdown_option2 != 'no' or 'yes':
    print ("sorry")