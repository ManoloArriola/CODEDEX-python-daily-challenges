def blood_moon(time):
    results = []
    
    hours, minutes = map(int, time.split(":"))
    
    for _ in range(3):
        minutes += 48
        
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60
        
        hours += 2
        
        hours = hours % 24
        
        formatted_time = f"{hours:02d}:{minutes:02d}"
        results.append(formatted_time)
    
    return results


user_time = ("01:00")
print(blood_moon(user_time))