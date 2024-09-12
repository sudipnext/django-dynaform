from django.shortcuts import render

# Create your views here.

def get_form_repeater_data(q):
    """
    Extracts data from the form repeater and returns a list of dictionaries containing the data

    """
    dict_obj = q
    # Iterate over the dictionary
    i = 0
    results = []
    unit_price = dict_obj.getlist("unit_price")
    crossed_price = dict_obj.getlist("crossed_price_productype")
    while i < len(dict_obj):
        try:
            variant_data = {}
            stock_quantities = []
            k = 0
            while True:
                try:
                    variant_data[
                        dict_obj[
                            "form-data[{i}][variant][{k}][attribute]".format(
                                i=i, k=k)
                        ]
                    ] = dict_obj["form-data[{i}][variant][{k}][value]".format(i=i, k=k)]
                    k += 1
                except KeyError:
                    break

            # Keep adding stocks until a KeyError is encountered
            j = 0
            while True:
                try:
                    stock_quantities.append(
                        dict_obj["form-data[{i}][stock][{j}][stocks]".format(
                            i=i, j=j)]
                    )
                    j += 1
                except KeyError:
                    break
            if variant_data:
                variant_data["stocks"] = stock_quantities
                variant_data["unit_price"] = unit_price[i]
                variant_data["crossed_price"] = crossed_price[i]
                results.append(variant_data)
            i += 1  # Increment i here
        except KeyError:
            break
    return results

def index(request):
    """
    Renders the index page

    """
    return render(request, "index.html")
