s=int(input())
hours=s//3600
mns=(s-(3600*hours))//60
sec=(s-(3600*hours))-(mns*60)
print(f"H:M:S-{hours}:{mns}:{sec}")