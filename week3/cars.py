  sales_car_by_year = {}
  model_car_by_year = {}
  global_sales = 0
  year = -1
 

if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    # TODO: also handle most popular car_year
    year = car["car_year"]

    if sales_car_by_year.get(str(year)) is None:
        sales_car_by_year[str(year)]={}
    else:
        sales_car_by_year[str(year)][car["car_model"]]=item["total_sales"]
  for year in sales_car_by_year:
    cars_year = sales_car_by_year[year]
    most_sales = ""
    sales = 0
    for model in cars_year:
        if cars_year[model]>sales:
            sales=cars_year[model]
            most_sales=model
            model_car_by_year[year]={'model':most_sales,'sales':sales}
    if not  model_car_by_year.get(str(year)) is None:
            print(year,model_car_by_year[str(year)])
  for year in model_car_by_year:
        sales = model_car_by_year[year]['sales']
        if (sales > global_sales):
            global_sales = sales
            global_year = year

