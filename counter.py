def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    try:
        handle = open(name)
    except:
        print("File name not found")
        exit()
    from_email = dict()
    for line in handle:
        line_split = line.split()

        if len(line_split) < 2 or line_split[0]!= 'From':
            continue
        else:
            if line_split[1] not in from_email:
                from_email[line_split[1]] = 1
            else:
               from_email[line_split[1]] += 1
    max_email_value = 0
    for key, value in from_email.items():
        if value > (max_email_value):
            max_email_value = value
            max_email = key
    print (max_email, max_email_value)


        
## if you want to test locally before you try to sync
## uncomment countEmail() and run > python counter.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##countEmail()
