def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  sales_car_by_year = {}
  model_car_by_year = {}
  global_sales = 0
  year = -1
  global_year = 0
  global_car = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    car = item["car"]
    all_cars.append([item["id"],format_car(car),f"${item_price}",item["total_sales"]])

    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    # TODO: also handle most popular car_year
    year = car["car_year"]

    if sales_car_by_year.get(str(year)) is None:
        sales_car_by_year[str(year)]={}
    else:
        sales_car_by_year[str(year)][car["car_model"]]={"sales":item["total_sales"],"make":car["car_make"]}
  for year in sales_car_by_year:
    cars_year = sales_car_by_year[year]
    most_sales = ""
    sales = 0
    #print(cars_year)
    for model in cars_year:
        if cars_year[model]["sales"]>sales:
            sales=cars_year[model]["sales"]
            most_sales=model
            model_car_by_year[year]={"car":cars_year[model],"model":model,"sales":sales}
    if not  model_car_by_year.get(str(year)) is None:
            print(year,model_car_by_year[str(year)])
  print("-")
  for year in model_car_by_year:
        sales = model_car_by_year[str(year)]['sales']
        if (sales > global_sales):
            global_car = model_car_by_year[str(year)]
            global_year = str(year)
            global_sales = sales
  print(global_year,global_car)
  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
    "The {} had the most sales: ${}".format(global_car['model'],global_sales),
  ]
  return summary

def main():
      data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report
  all_cars.insert(0,['ID','Car','Price','Total Sales'])
  formated = ""
  for_email = ""
  for s in summary:
    formated = formated + s + "\n"
    for_email = for_email + s + "<br/>"

  reports.generate("/tmp/cars.pdf", "Sales summart for the last month", for_email, all_cars)
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = formated
  message = emails.generate(sender, receiver, subject, body, "/tmp/cars.pdf")
  emails.send(message)

