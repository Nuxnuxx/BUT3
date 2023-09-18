namespace Calculator.Test;
using Calc = calculator.Calculator;

[TestClass]
public class UnitTest1
{
    [TestMethod]
  public void TestAdd(){
    Calc calculator = new Calc();

    int result = calculator.Add(5, 3);

    Assert.AreEqual(8, result);
  }
}
