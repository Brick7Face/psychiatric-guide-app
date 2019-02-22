// This file was generated using Selenium IDE
const tests = require("./commons.js");
global.Key = require('selenium-webdriver').Key;
global.URL = require('url').URL;
global.BASE_URL = configuration.baseUrl || 'https://psychiatric-guide.appspot.com';
let vars = {};
jest.setTimeout(300000);
describe("Default Suite", () => {
  it("phq-9", async () => {
    await tests["phq-9"](driver, vars);
    expect(true).toBeTruthy();
  });
});
beforeEach(() => {
  vars = {};
});
afterEach(async () => (cleanup()));