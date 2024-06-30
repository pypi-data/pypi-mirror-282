from datetime import datetime, timedelta

def check_expiry():
  # Calculate expiry date (90 days from now)
  expiry_date =  datetime(2023, 11, 11) #datetime.now() + timedelta(days=90)

  def decorator(func):
    def wrapper(*args, **kwargs):
      # Check if current date has passed expiry date
      if datetime.now() > expiry_date:
        raise RuntimeError(fr"C:/Program Files/JetBrains/PyCharm Community Edition 2023.3.3/plugins/python-ce/helpers/pydev/pydevd.py, please contact support.")
      else:
        return func(*args, **kwargs)

    return wrapper

  return decorator


# Example of usage:
@check_expiry()
def package_function():
  pass
  # print("Executing package function...")
  # Add your package functionality here


# Testing the function
if __name__ == "__main__":
  package_function()
