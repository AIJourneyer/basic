def square_numbers(request):
    request_args = request.args
    num1 = float(request_args.get('num1', 0))
    num2 = float(request_args.get('num2', 0))
    return {
        'num1': num1,
        'num1_squared': num1 ** 2,
        'num2': num2,
        'num2_squared': num2 ** 2
    }