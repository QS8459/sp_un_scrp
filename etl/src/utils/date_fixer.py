from datetime import datetime, timedelta;
from src import ru_month
def date_cleaner(date):
    date = date.strip().replace(',','')
    d = date.split(' ')

    for i in range(0,len(ru_month)):
        if d[1] in ru_month[i]:
            return (
                # Year
                str(datetime.now().year if len(d) == 3 else d[2]) + '-'
                # Moth
                + str(f'0{i+1}' if i+1 < 10 else f"{i+1}") + '-'
                # Time
                + d[0] + " " + d[-1] + ":00"
            )
    if d[0] in 'сегодня':
        return datetime.now().strftime('%Y-%m-%d ') + d[1] + ":00"
    if d[0] in 'вчера':
        return (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d ') + d[1] + ':00'


