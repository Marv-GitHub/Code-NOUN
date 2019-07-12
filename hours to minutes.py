print("convert to hours:minutes:seconds")
given_secs=int(input("please input number of seconds: "))
hours= given_secs//3600
rem_hours=given_secs%3600
minutes= rem_hours//60
seconds= rem_hours%60
print(hours, minutes, seconds, sep=":")
