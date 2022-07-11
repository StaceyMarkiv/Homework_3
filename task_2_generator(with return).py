"""Я сделала данный вариант, так как в описании ДЗ было указано, что функция должна вернуть список через return.
Но так как генератор все же должен возвращать результаты через yield, то я сделала также и другой вариант
решения, более правильный."""
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        delta: timedelta = timedelta(days=1)
        show_dates_total: List[datetime] = []

        for date_pair in self.dates:
            start_date: datetime = date_pair[0]
            end_date: datetime = date_pair[1]

            if start_date > end_date:
                end_date, start_date = start_date, end_date

            show_period: List[datetime] = []
            while start_date <= end_date:
                show_period.append(start_date)
                start_date += delta
            show_dates_total.extend(show_period)
        return show_dates_total


if __name__ == '__main__':
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)
