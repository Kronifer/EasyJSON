import func

func.init("test.json")

func.addData("a", "b")
func.addData("b", "c")
func.addData("c", "d")

func.groupData(["a", "b", "c"], "letter")

valueList = func.getGroupData("letter")

print(valueList)
