season_by_month = {
"зима": list([1, 2, 12]),
"весна": list([3, 4, 5]),
"лето": list([6, 7, 8]),
"осень": list([9, 10, 11]),
}
month_input = int(input())
season_output = ''
for season in season_by_month:
    if month_input in season_by_month[season]:
        season_output = season
        break
    else:
        season_output = "Месяца с данным порядковым номером не существует"

print(season_output)
