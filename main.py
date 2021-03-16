second=int(input"enter the value for seconds:"))



day=(((second//60)//60)//24)
print(f"total day for given seconds:{day}")


hour=((second//60)//60)
print(f"total hours for given second:{hour}")



minute=(second //60)
print(f"total minute for given second:{minute}")


