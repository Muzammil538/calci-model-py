def main(case):
  def cal():
    inp_cal = input("Enter the calculation : ")
    try:
      print(eval(inp_cal))
    except Exception as e:
      print(e)
      
  if(case == 1):
    
    ds = 1
    while(ds):
      cal()


if __name__ == "__main__":
  def_switch = 0 # switch is off

  print("Select the option from the menu ")
  print("1. Toggle the switch")
  print("2. Mode switch")
  inp_btn = int(input("Enter : "))
  main(inp_btn)