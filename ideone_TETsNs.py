yr=int(raw_input())
if yr%4==0:
  if yr%100==0:
    if yr%400==0:
      print "leap"
    else:
      print"not"
  else:
    print"leap"
else:
  print"not"