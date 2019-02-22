const utils = require("./utils.js");
const tests = {};
tests["phq-9"] = async (driver, vars, opts = {}) => {
  await driver.get((new URL("/", BASE_URL)).href);
  await driver.manage().window().setRect({
    width: 968,
    height: 1040
  });
  await driver.wait(until.elementLocated(By.id(`id_username`)), configuration.timeout);
  await driver.findElement(By.id(`id_username`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.id(`id_username`)), configuration.timeout);
  await driver.findElement(By.id(`id_username`)).then(element => {
    return element.clear().then(() => {
      return element.sendKeys(`admin`);
    });
  });
  await driver.wait(until.elementLocated(By.id(`id_password`)), configuration.timeout);
  await driver.findElement(By.id(`id_password`)).then(element => {
    return element.clear().then(() => {
      return element.sendKeys(`adminpassword`);
    });
  });
  await driver.wait(until.elementLocated(By.css(`.btn`)), configuration.timeout);
  await driver.findElement(By.css(`.btn`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.linkText(`PHQ-9`)), configuration.timeout);
  await driver.findElement(By.linkText(`PHQ-9`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.continue-button`)), configuration.timeout);
  await driver.findElement(By.css(`.continue-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(2) > #choice-container > .choice:nth-child(2) input`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(2) > #choice-container > .choice:nth-child(2) input`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.next-button:nth-child(1)`)), configuration.timeout);
  await driver.findElement(By.css(`.next-button:nth-child(1)`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(3) > #choice-container > .choice:nth-child(3) input`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(3) > #choice-container > .choice:nth-child(3) input`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(3) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(3) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(4) .choice:nth-child(4) > label`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(4) .choice:nth-child(4) > label`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(4) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(4) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(5) .choice:nth-child(2) > label`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(5) .choice:nth-child(2) > label`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(5) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(5) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(6) .choice:nth-child(1) > label`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(6) .choice:nth-child(1) > label`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(6) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(6) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(7) .choice:nth-child(3) > label`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(7) .choice:nth-child(3) > label`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(7) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(7) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(8) .choice:nth-child(4) > label`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(8) .choice:nth-child(4) > label`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(8) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(8) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(9) .choice:nth-child(3) > label`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(9) .choice:nth-child(3) > label`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(9) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(9) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(10) > #choice-container > .choice:nth-child(2) input`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(10) > #choice-container > .choice:nth-child(2) input`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(10) .next-button`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(10) .next-button`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.question:nth-child(11) > #choice-container > .choice:nth-child(3) input`)), configuration.timeout);
  await driver.findElement(By.css(`.question:nth-child(11) > #choice-container > .choice:nth-child(3) input`)).then(element => {
    return element.click();
  });
  await driver.wait(until.elementLocated(By.css(`.submit-button`)), configuration.timeout);
  await driver.findElement(By.css(`.submit-button`)).then(element => {
    return element.click();
  });
}
module.exports = tests;