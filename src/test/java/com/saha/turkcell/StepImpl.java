package com.saha.turkcell;

import com.saha.turkcell.helper.RandomString;
import com.saha.turkcell.helper.StoreHelper;
import com.saha.turkcell.model.SelectorInfo;
import com.thoughtworks.gauge.ExecutionContext;
import com.thoughtworks.gauge.Step;
import io.appium.java_client.AppiumDriver;
import io.appium.java_client.MobileBy;
import io.appium.java_client.MobileElement;
import io.appium.java_client.TouchAction;
import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.android.nativekey.AndroidKey;
import io.appium.java_client.android.nativekey.KeyEvent;
import io.appium.java_client.ios.IOSDriver;
import io.appium.java_client.remote.AndroidMobileCapabilityType;
import io.appium.java_client.remote.IOSMobileCapabilityType;
import io.appium.java_client.remote.MobileCapabilityType;
import io.appium.java_client.remote.MobilePlatform;
import io.appium.java_client.touch.WaitOptions;
import io.appium.java_client.touch.offset.PointOption;
import org.apache.commons.lang.StringUtils;
import org.apache.log4j.PropertyConfigurator;
import org.assertj.core.api.Assertions;
import org.junit.Assert;
import org.junit.Before;
import org.openqa.selenium.*;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.openqa.selenium.support.ui.ExpectedCondition;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.FluentWait;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.slf4j.LoggerFactory;
import org.slf4j.impl.Log4jLoggerAdapter;

import javax.annotation.Nullable;
import java.net.MalformedURLException;
import java.net.URL;
import java.text.NumberFormat;
import java.text.ParseException;
import java.time.Duration;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;
import java.util.ResourceBundle;

import static java.time.Duration.ofMillis;

public class StepImpl extends HookImpl {
    ResourceBundle kartBilgileri;

    private static Log4jLoggerAdapter logger = (Log4jLoggerAdapter) LoggerFactory.getLogger(StepImpl.class);

    public StepImpl() {

        PropertyConfigurator.configure(StepImpl.class.getClassLoader().getResource("log4j.properties"));
    }

    public List<MobileElement> findElements(By by) throws Exception {
        List<MobileElement> webElementList = null;
        try {
            webElementList = appiumFluentWait.until(new ExpectedCondition<List<MobileElement>>() {
                @Nullable
                @Override
                public List<MobileElement> apply(@Nullable WebDriver driver) {
                    List<MobileElement> elements = driver.findElements(by);
                    return elements.size() > 0 ? elements : null;
                }
            });
            if (webElementList == null) {
                throw new NullPointerException(String.format("by = %s Web element list not found", by.toString()));
            }
        } catch (Exception e) {
            throw e;
        }
        return webElementList;
    }

    public List<MobileElement> findElementsWithoutAssert(By by) {

        List<MobileElement> mobileElements = null;
        try {
            mobileElements = findElements(by);
        } catch (Exception e) {
        }
        return mobileElements;
    }

    public List<MobileElement> findElementsWithAssert(By by) {

        List<MobileElement> mobileElements = null;
        try {
            mobileElements = findElements(by);
        } catch (Exception e) {
            Assertions.fail("by = %s Elements not found ", by.toString());
            e.printStackTrace();
        }
        return mobileElements;
    }


    public MobileElement findElement(By by) throws Exception {
        MobileElement mobileElement;
        try {
            mobileElement = findElements(by).get(0);
        } catch (Exception e) {
            throw e;
        }
        return mobileElement;
    }

    public MobileElement findElementWithoutAssert(By by) {
        MobileElement mobileElement = null;
        try {
            mobileElement = findElement(by);
        } catch (Exception e) {
            //   e.printStackTrace();
        }
        return mobileElement;
    }

    public MobileElement findElementWithAssertion(By by) {
        MobileElement mobileElement = null;
        try {
            mobileElement = findElement(by);
        } catch (Exception e) {
            Assertions.fail(mobileElement.getAttribute("value") + " " + "by = %s Element not found ", by.toString());
            e.printStackTrace();
        }
        return mobileElement;
    }

    public MobileElement findElementByKeyWithoutAssert(String key) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);

        MobileElement mobileElement = null;
        try {
            mobileElement = selectorInfo.getIndex() > 0 ? findElements(selectorInfo.getBy())
                    .get(selectorInfo.getIndex()) : findElement(selectorInfo.getBy());
        } catch (Exception e) {
            e.printStackTrace();
        }
        return mobileElement;
    }

    public MobileElement findElementByKey(String key) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);

        MobileElement mobileElement = null;
        try {
            mobileElement = selectorInfo.getIndex() > 0 ? findElements(selectorInfo.getBy())
                    .get(selectorInfo.getIndex()) : findElement(selectorInfo.getBy());
        } catch (Exception e) {
            Assertions.fail("key = %s by = %s Element not found ", key, selectorInfo.getBy().toString());
            e.printStackTrace();
        }
        return mobileElement;
    }


    public List<MobileElement> findElemenstByKeyWithoutAssert(String key) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        List<MobileElement> mobileElements = null;
        try {
            mobileElements = findElements(selectorInfo.getBy());
        } catch (Exception e) {
            e.printStackTrace();
        }
        return mobileElements;
    }

    public void tapPointElementWithPress(String key, int x, int y) {

        tapPointElementWithPress(key, x, y, 250);
    }

    public void tapPointElementWithPress(String key, int x, int y, long millis) {

        MobileElement mobileElement = findElementByKey(key);
        Point location = mobileElement.getLocation();
        Dimension dimension = mobileElement.getSize();
        int tapX = location.x + (dimension.width * x) / 100;
        int tapY = location.y + (dimension.height * y) / 100;
        TouchAction touchAction = new TouchAction(appiumDriver);
        touchAction.press(PointOption.point(tapX, tapY))
                .waitAction(WaitOptions.waitOptions(Duration.ofMillis(millis)))
                .press(PointOption.point(tapX, tapY)).release().perform();
        logger.info(key + " elementinin " + tapX + " ve " + tapY + " koordinatlarına tıklanıyor...");
    }

    public FluentWait<AppiumDriver<MobileElement>> setFluentWait(int timeout) {
        return new FluentWait<AppiumDriver<MobileElement>>(appiumDriver).withTimeout(Duration.ofSeconds(timeout))
                .pollingEvery(Duration.ofMillis(250))
                .ignoring(NoSuchElementException.class);
    }

    public boolean isElementClickable(String key, int timeout) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        try {
            setFluentWait(timeout).until(ExpectedConditions.elementToBeClickable(selectorInfo.getBy()));
            logger.info("true");
            return true;
        } catch (Exception e) {
            logger.info("false");
            return false;
        }
    }

    public List<MobileElement> findElemenstByKey(String key) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        List<MobileElement> mobileElements = null;
        try {
            mobileElements = findElements(selectorInfo.getBy());
        } catch (Exception e) {
            Assertions.fail("key = %s by = %s Elements not found ", key, selectorInfo.getBy().toString());
            e.printStackTrace();
        }
        return mobileElements;
    }

    @Step("<key> elementinin <x> ile <y> koordinatına tıkla")
    public void tapPointElementByPress(String key, int x, int y) {
        tapPointElementWithPress(key, x, y);
    }


    @Step({"Değeri <text> e eşit olan elementli bul ve tıkla",
            "Find element text equals <text> and click"})
    public void clickByText(String text) {
        findElementWithAssertion(By.xpath(".//*[contains(@text,'" + text + "')]")).click();
    }

    @Step({"İçeriği <value> e eşit olan elementli bul ve tıkla",
            "Find element value equals <value> and click"})
    public void clickByValue(String value) {
        findElementWithAssertion(MobileBy.xpath(".//*[contains(@value,'" + value + "')]")).click();
    }

    @Step({"Değeri <text> e eşit olan <index>. elementi bul ve tıkla"})
    public void clickByText(String text, int index) {
        findElementWithAssertion(By.xpath("(.//*[contains(@text,'" + text + "')])[" + index + "]")).click();
    }

    @Step({"İçeriği <value> e eşit olan <index>. elementi bul ve tıkla"})
    public void clickByValue(String value, int index) {
        findElementWithAssertion(MobileBy.xpath("(.//*[contains(@value,'" + value + "')])[" + index + "]")).click();
    }

    @Step("<key> elementinin <index> .li elementi bul ve tıkla")
    public void clickByKeyIndex(String key, int index) {
        findElementsWithoutAssert(selector.getSelectorInfo(key).getBy()).get(index).click();
    }

    @Step("Uygulamanın açıldığını kontrol et")
    public void checkApp() throws InterruptedException {
        logger.info("Uygulamanin acildigini kontrol et");
        if (appiumDriver instanceof AndroidDriver) {
            existClickByKey("reddetButonu");
            clickBybackButton();
            waitBySecond(10);
        } else {
            existClickByKey("reddetButonu");
            waitBySecond(10);
        }

    }


    @Step({"<key> li elementi bul ve tıkla", "Click element by <key>"})
    public void clickByKey(String key) throws InterruptedException {
        waitBySecond(2);
      //  doesElementExistByKey(key, 5);
        //       logger.info("appiumDriver.getPageSource().contains(key)");

        isElementClickable(key, 30);
        findElementByKey(key).click();
        //    MobileElement me = findElementByKey(key);
        //  tapElementWithCoordinate(me.getLocation().x, me.getLocation().y);
        logger.info(key + "elemente tıkladı");


    }

    @Step({"<key> li element sayfada bulunuyor mu kontrol et"})
    public void existElement(String key) {
        doesElementExistByKey(key, 5);
        Assert.assertTrue("'"+key+"' element sayfada bulunamadı !", findElementByKey(key).isDisplayed());

    }

    @Step("giris yap butonuna tikla")
    public void clickLoginButton() throws InterruptedException {
        newWebDriverWait(30, 1000);
        clickByKey("girisYapButonu");
        //findElementWithAssertion(By.id("com.ttech.android.onlineislem:id/buttonPasswordContinue")).click();
        waitBySecond(5);
        //existClickByKey("dinamikKartlarıKapatmaIkonu");
    }

    @Step("<key> li elementi bul ve varsa <text> yaz")
    public void existWriteByKey(String key, String text) throws InterruptedException {

        MobileElement element;

        element = findElementByKeyWithoutAssert(key);

        if (element != null) {
            System.out.println("  varsa yaza girdi");
            element.sendKeys(text);
        }
        waitBySecond(2);
    }


    @Step({"<key> li elementi bul ve varsa tıkla", "Click element by <key> if exist"})
    public void existClickByKey(String key) throws InterruptedException {

        if (doesElementExistByKey(key, 5)) {

            System.out.println("  varsa tıklaya girdi");
            clickByKey(key);
        }
    }

    @Step("<number> numarası sayfada bulunuyormu kontrol et")
    public void findByNumber(String number) {
        String xpath = "//android.widget.TextView[@content-desc='" + number + "']";
        Assert.assertTrue("Element sayfada bulunamadı !",
                appiumDriver.findElement(By.xpath(xpath)).isDisplayed());


    }

    @Step({"<key> li elementi bul ve varsa dokun", "Click element by <key> if exist"})
    public void existTapByKey(String key) {

        WebElement element = null;
        try {
            element = findElementByKey(key);
        } catch (Exception e) {
            e.printStackTrace();
        }
        if (element != null) {
            element.click();
        }
    }

    @Step({"sayfadaki <X> <Y>  alana dokun"})
    public void coordinateTap(int X, int Y) {

        Dimension dimension = appiumDriver.manage().window().getSize();
        int width = dimension.width;
        int height = dimension.height;

        TouchAction action = new TouchAction(appiumDriver);
        action.tap(PointOption.point((width * X) / 100, (height * Y) / 100))
                .release().perform();

    }

    @Step({"sayfadaki <X> <Y>  alana tıkla"})


    public void tapByCoordinates(int X, int Y) {

        Dimension dimension = appiumDriver.manage().window().getSize();
        int width = dimension.width;
        int height = dimension.height;


        TouchAction action = new TouchAction(appiumDriver);
        action.tap(PointOption.point((width * X) / 100, (height * Y) / 100))
                .perform();

    }


    @Step({"<key> li elementi bul, temizle ve <text> değerini yaz",
            "Find element by <key> clear and send keys <text>"})
    public void sendKeysByKey(String key, String text) {
        MobileElement webElement = findElementByKey(key);

        webElement.clear();
        webElement.setValue(text);
    }


    @Step({"<key> li elementi bul ve <text> değerini yaz",
            "Find element by <key> and send keys <text>"})
    public void sendKeysByKeyNotClear(String key, String text) {
        if (text.contains("KrediKartNo")) {
            text = HookImpl.kartBilgileri.getString(cardInformationNo() + "KartNo");
        } else if (text.contains("Cvv")) {
            text = HookImpl.kartBilgileri.getString(cardInformationNo() + "Cvc");
        } else if (text.contains("Kullanıcı Adı")) {
            System.out.println(cardInformationNo() + "AdSoyad");
            text = HookImpl.kartBilgileri.getString(cardInformationNo() + "AdSoyad");
        }
        doesElementExistByKey(key, 5);
        findElementByKey(key).setValue(text);
        //  sendKeysValueOfClear(key,text);

    }

    @Step({"<key> li elementi bul tikla ve <text> değerini yaz",
            "Find element by <key> and send keys <text>"})
    public void sendKeysByKeyNotClearAfterClick(String key, String text) {
        doesElementExistByKey(key, 5);
        findElementByKey(key).click();
        findElementByKey(key).setValue(text);
        //  sendKeysValueOfClear(key,text);

    }


    @Step("<key> li elementi bul ve <text> değerini tek tek yaz")
    public void sendKeysValueOfClear(String key, String text) {
        MobileElement me = findElementByKey(key);
        me.clear();
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            me.sendKeys(String.valueOf(c));
        }
        System.out.println("'" + text + "' written to '" + key + "' element.");

    }

    @Step("<key> elementinin koordinatlarına x=<x> y=<y> degerlerini ekleyerek tıkla ve <text> yaz")
    public void textWrite(String key, int x, int y, String text) {
        MobileElement me = findElementByKey(key);
        tapElementWithCoordinate(me.getLocation().x + x, me.getLocation().y + y);
        //me.sendKeys(text);
        sendKeysByKeyNotClear(key, text);

    }


    @Step({"<key> li elementi bul ve değerini <saveKey> olarak sakla",
            "Find element by <key> and save text <saveKey>"})
    public void saveTextByKey(String key, String saveKey) {
        StoreHelper.INSTANCE.saveValue(saveKey, findElementByKey(key).getText());
    }

    @Step({"<key> li elementi bul ve değerini <saveKey> saklanan değer ile karşılaştır",
            "Find element by <key> and compare saved key <saveKey>"})
    public void equalsSaveTextByKey(String key, String saveKey) {
        Assert.assertEquals(StoreHelper.INSTANCE.getValue(saveKey), findElementByKey(key).getText());
    }


    @Step({"<key> li ve değeri <text> e eşit olan elementli bul ve tıkla",
            "Find element by <key> text equals <text> and click"})
    public void clickByIdWithContains(String key, String text) {
        List<MobileElement> elements = findElemenstByKey(key);
        for (MobileElement element : elements) {
            logger.info("Text !!!" + element.getText());
            if (element.getText().toLowerCase().contains(text.toLowerCase())) {
                element.click();
                break;
            }
        }
    }

    @Step({"<key> li ve değeri <text> e eşit olan elementli bulana kadar swipe et ve tıkla",
            "Find element by <key> text equals <text> swipe and click"})
    public void clickByKeyWithSwipe(String key, String text) throws InterruptedException {
        boolean find = false;
        int maxRetryCount = 10;
        while (!find && maxRetryCount > 0) {
            List<MobileElement> elements = findElemenstByKey(key);
            for (MobileElement element : elements) {
                if (element.getText().contains(text)) {
                    element.click();
                    find = true;
                    break;
                }
            }
            if (!find) {
                maxRetryCount--;
                if (appiumDriver instanceof AndroidDriver) {
                    swipeUpAccordingToPhoneSize();
                    waitBySecond(1);
                } else {
                    swipeDownAccordingToPhoneSize();
                    waitBySecond(1);
                }
            }
        }
    }

    @Step({"<key> li elementi bulana kadar swipe et ve tıkla",
            "Find element by <key>  swipe and click"})
    public void clickByKeyWithSwipe(String key) throws InterruptedException {
        int maxRetryCount = 10;
        while (maxRetryCount > 0) {
            List<MobileElement> elements = findElemenstByKey(key);
            if (elements.size() > 0) {
                if (elements.get(0).isDisplayed() == false) {
                    maxRetryCount--;
                    swipeDownAccordingToPhoneSize();
                    waitBySecond(1);

                } else {
                    elements.get(0).click();
                    logger.info(key + " elementine tıklandı");
                    break;
                }
            } else {
                maxRetryCount--;
                swipeDownAccordingToPhoneSize();
                waitBySecond(1);
            }

        }
    }


    private int getScreenWidth() {
        return appiumDriver.manage().window().getSize().width;
    }

    private int getScreenHeight() {
        return appiumDriver.manage().window().getSize().height;
    }

    private int getScreenWithRateToPercent(int percent) {
        return getScreenWidth() * percent / 100;
    }

    private int getScreenHeightRateToPercent(int percent) {
        return getScreenHeight() * percent / 100;
    }


    public void swipeDownAccordingToPhoneSize(int startXLocation, int startYLocation, int endXLocation, int endYLocation) {
        startXLocation = getScreenWithRateToPercent(startXLocation);
        startYLocation = getScreenHeightRateToPercent(startYLocation);
        endXLocation = getScreenWithRateToPercent(endXLocation);
        endYLocation = getScreenHeightRateToPercent(endYLocation);

        new TouchAction(appiumDriver)
                .press(PointOption.point(startXLocation, startYLocation))
                .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                .moveTo(PointOption.point(endXLocation, endYLocation))
                .release()
                .perform();
    }

    @Step({"<key> id'li elementi bulana kadar <times> swipe yap ",
            "Find element by <key>  <times> swipe "})
    public void swipeDownUntilSeeTheElement(String element, int limit) throws InterruptedException {
        for (int i = 0; i < limit; i++) {
            List<MobileElement> meList = findElementsWithoutAssert(By.id(element));
            meList = meList != null ? meList : new ArrayList<MobileElement>();
            logger.info(i + ". swipe yapiliyor");
            if (meList.size() > 0 &&
                    meList.get(0).getLocation().x <= getScreenWidth() &&
                    meList.get(0).getLocation().y <= getScreenHeight()) {
                break;
            } else {
                swipeDownAccordingToPhoneSize(50, 80, 50, 30);
                waitBySecond(1);

                break;
            }
        }
    }


    @Step({"<key> li elementi bulana kadar swipe et",
            "Find element by <key>  swipe "})
    public void findByKeyWithSwipe(String key) {
        int maxRetryCount = 10;
        while (maxRetryCount > 0) {
            List<MobileElement> elements = findElemenstByKey(key);
            if (elements.size() > 0) {
                if (elements.get(0).isDisplayed() == false) {
                    maxRetryCount--;

                    swipeDownAccordingToPhoneSize();

                } else {
                    System.out.println(key + " element bulundu");
                    break;
                }
            } else {
                maxRetryCount--;
                swipeDownAccordingToPhoneSize();

            }

        }
    }


    @Step(" <yön> yönüne swipe et")
    public void swipe(String yon) {

        Dimension d = appiumDriver.manage().window().getSize();
        int height = d.height;
        int width = d.width;

        if (yon.equals("SAĞ")) {

            int swipeStartWidth = (width * 80) / 100;
            int swipeEndWidth = (width * 30) / 100;

            int swipeStartHeight = height / 2;
            int swipeEndHeight = height / 2;

            //appiumDriver.swipe(swipeStartWidth, swipeStartHeight, swipeEndWidth, swipeEndHeight, 1000);
            new TouchAction(appiumDriver)
                    .press(PointOption.point(swipeStartWidth, swipeStartHeight))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(swipeEndWidth, swipeEndHeight))
                    .release()
                    .perform();
        } else if (yon.equals("SOL")) {

            int swipeStartWidth = (width * 30) / 100;
            int swipeEndWidth = (width * 80) / 100;

            int swipeStartHeight = height / 2;
            int swipeEndHeight = height / 2;

            //appiumDriver.swipe(swipeStartWidth, swipeStartHeight, swipeEndWidth, swipeEndHeight, 1000);

            new TouchAction(appiumDriver)
                    .press(PointOption.point(swipeStartWidth, swipeStartHeight))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(swipeEndWidth, swipeEndHeight))
                    .release()
                    .perform();

        }
    }

    @Step({"<key> li elementi bul yoksa <message> mesajını hata olarak göster",
            "Find element by <key> if not exist show error message <message>"})
    public void isElementExist(String key, String message) throws InterruptedException {
        waitBySecond(3);
        Assert.assertTrue(message, findElementByKey(key) != null);
    }

    @Step({"<key> li elementi bul varsa <message> mesajını hata olarak göster",
            "Find element by <key> if not exist show error message <message>"})
    public void isNotElementExist(String key, String message) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        MobileElement mobileElement = null;
        try {
            mobileElement = selectorInfo.getIndex() > 0 ? findElements(selectorInfo.getBy())
                    .get(selectorInfo.getIndex()) : findElement(selectorInfo.getBy());
            Assert.fail(message);
        } catch (Exception e) {
            return;
        }
    }

    @Step({"<key> li elementin değeri <text> e içerdiğini kontrol et",
            "Find element by <key> and text contains <text>"})
    public void containsTextByKey(String key, String text) {
        By by = selector.getElementInfoToBy(key);
        Assert.assertTrue(appiumFluentWait.until(new ExpectedCondition<Boolean>() {
            private String currentValue = null;

            @Override
            public Boolean apply(WebDriver driver) {
                try {
                    currentValue = driver.findElement(by).getText();
                    return currentValue.contains(text);
                } catch (Exception e) {
                    return false;
                }
            }

            @Override
            public String toString() {
                return String.format("text contains be \"%s\". Current text: \"%s\"", text, currentValue);
            }
        }));
    }

    @Step({"<key> li elementin değeri <text> e eşitliğini kontrol et",
            "Find element by <key> and text equals <text>"})
    public void equalsTextByKey(String key, String text) {
        Assert.assertTrue(appiumFluentWait.until(
                ExpectedConditions.textToBe(selector.getElementInfoToBy(key), text)));
    }

    @Step({"<seconds> saniye bekle", "Wait <second> seconds"})
    public void waitBySecond(int seconds) throws InterruptedException {
        Thread.sleep(seconds * 1000);
    }

    public void swipeUpAccordingToPhoneSize() {
        if (appiumDriver instanceof AndroidDriver) {
            Dimension d = appiumDriver.manage().window().getSize();
            int height = d.height;
            int width = d.width;
            System.out.println(width + "  " + height);

            int swipeStartWidth = width / 2, swipeEndWidth = width / 2;
            int swipeStartHeight = (height * 23) / 100;
            int swipeEndHeight = (height * 83) / 100;
            //appiumDriver.swipe(swipeStartWidth, swipeStartHeight, swipeEndWidth, swipeEndHeight, 1000);
            new TouchAction((AndroidDriver) appiumDriver)
                    .press(PointOption.point(swipeStartWidth, swipeEndHeight))
                    .waitAction(WaitOptions.waitOptions(ofMillis(2000)))
                    .moveTo(PointOption.point(swipeEndWidth, swipeStartHeight))
                    .release()
                    .perform();
        } else {
            Dimension d = appiumDriver.manage().window().getSize();
            int height = d.height;
            int width = d.width;

            int swipeStartWidth = width / 2, swipeEndWidth = width / 2;
            int swipeStartHeight = (height * 25) / 100;
            int swipeEndHeight = (height * 85) / 100;
            //appiumDriver.swipe(swipeStartWidth, swipeStartHeight, swipeEndWidth, swipeEndHeight, 1000);
            new TouchAction(appiumDriver)
                    .press(PointOption.point(swipeStartWidth, swipeEndHeight))
                    .waitAction(WaitOptions.waitOptions(ofMillis(2000)))
                    .moveTo(PointOption.point(swipeEndWidth, swipeStartHeight))
                    .release()
                    .perform();
        }
    }


    public void swipeDownAccordingToPhoneSize() {
        if (appiumDriver instanceof AndroidDriver) {
            Dimension d = appiumDriver.manage().window().getSize();
            int height = d.height;
            int width = d.width;

            int swipeStartWidth = width / 2, swipeEndWidth = width / 2;
            int swipeStartHeight = (height * 90) / 100;
            int swipeEndHeight = (height * 50) / 100;
            //appiumDriver.swipe(swipeStartWidth, swipeStartHeight, swipeEndWidth, swipeEndHeight, 1000);
            new TouchAction(appiumDriver)
                    .press(PointOption.point(swipeStartWidth, swipeStartHeight))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(swipeEndWidth, swipeEndHeight))
                    .release()
                    .perform();
        } else {
            Dimension d = appiumDriver.manage().window().getSize();
            int height = d.height;
            int width = d.width;

            int swipeStartWidth = width / 2, swipeEndWidth = width / 2;
            int swipeStartHeight = (height * 90) / 100;
            int swipeEndHeight = (height * 40) / 100;
            // appiumDriver.swipe(swipeStartWidth, swipeStartHeight, swipeEndWidth, swipeEndHeight, 1000);
            new TouchAction(appiumDriver)
                    .press(PointOption.point(swipeStartWidth, swipeStartHeight))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(swipeEndWidth, swipeEndHeight))
                    .release()
                    .perform();
        }
    }

    public boolean isElementPresent(By by) {
        return findElementWithoutAssert(by) != null;
    }


    @Step({"<times> kere aşağıya kaydır", "Swipe times <times>"})
    public void swipe(int times) throws InterruptedException {
        for (int i = 0; i < times; i++) {
            swipeDownAccordingToPhoneSize();
            waitBySecond(3);

            System.out.println("-----------------------------------------------------------------");
            System.out.println("SWİPE EDİLDİ");
            System.out.println("-----------------------------------------------------------------");

        }
    }


    @Step({"<times> kere yukarı doğru kaydır", "Swipe up times <times>"})
    public void swipeUP(int times) throws InterruptedException {
        for (int i = 0; i < times; i++) {
            swipeUpAccordingToPhoneSize();
            waitBySecond(3);

            System.out.println("-----------------------------------------------------------------");
            System.out.println("SWİPE EDİLDİ");
            System.out.println("-----------------------------------------------------------------");

        }
    }


    @Before
    public void setUp() throws Exception {

    }

    @Step({"Klavyeyi kapat", "Hide keyboard"})
    public void hideAndroidKeyboard() {
        if (devicesPlatformAnd()) {
            try {


                appiumDriver.hideKeyboard();

            } catch (Exception ex) {
                logger.error("Klavye kapatılamadı ", ex.getMessage());
            }
        } else {
            try {
                existClickByKey("ıosKeyboardDone");

                // findElementByKey("ıosKeyboardDone").click();
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }


    @Step({"<text> değerini sayfa üzerinde olup olmadığını kontrol et."})
    public void getPageSourceFindWord(String text) {
        Assert.assertTrue(text + " sayfa üzerinde bulunamadı.",
                appiumDriver.getPageSource().contains(text));

        logger.info(text + " sayfa üzerinde bulundu");
    }


    @Step({"<length> uzunlugunda random bir kelime üret ve <saveKey> olarak sakla"})
    public void createRandomNumber(int length, String saveKey) {
        StoreHelper.INSTANCE.saveValue(saveKey, new RandomString(length).nextString());
    }

    @Step("geri butonuna bas")
    public void clickBybackButton() {
        if (!localAndroid) {
            backPage();
        } else {
            ((AndroidDriver) appiumDriver).pressKey(new KeyEvent().withKey(AndroidKey.BACK));
        }

    }

    @Step("Tamam butonuna tıkla")
    public void clickOKButton() {

        newWebDriverWait(30, 1000);

        MobileElement me = (MobileElement) appiumFluentWait.until(ExpectedConditions.presenceOfElementLocated(By.id("com.ttech.android.onlineislem:id/btn_confirm")));
        me.click();
    }


    @Step("Login  kontrol")
    public void LoginControl() throws InterruptedException {
        if (isElementPresent(By.id("com.ttech.android.onlineislem:id/textViewLoginMsisdn"))) {


            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/textViewLoginMsisdn")).click();
            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/textViewGoToProfile")).click();
            waitBySecond(2);
            swipe(1);
            waitBySecond(10);
            findElementWithoutAssert(By.xpath("//android.widget.TextView[@content-desc='Çıkış']")).click();
            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/buttonPositive")).click();
            existClickByKey("ızınVer");

        } else {

            logger.info("Sisteme login olma işlemi başladı");

        }
    }

    @Step("Anasayfa widget kontrolü")
    public void maninPagewidgetControl() throws InterruptedException {
        waitBySecond(3);
        if (isElementPresent(By.id("com.ttech.android.onlineislem:id/image_selocan_right"))) {

            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/navigation_myaccount")).click();
            waitBySecond(2);
            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/navigation_shop")).click();
            waitBySecond(2);
            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/navigation_support")).click();
            waitBySecond(2);
            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/imageViewProfilIcon")).click();
            waitBySecond(2);
            findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/linearLayoutNotificationsn")).click();

        } else {
            logger.info("Widget görülmedi !!!!!");
        }
    }

    @Step("Çıkış yap butonuna tıkla")
    public void Clicklogout() throws InterruptedException {
        waitBySecond(2);
        swipe(1);
        findElementWithoutAssert(By.xpath("//android.widget.TextView[@content-desc='Çıkış']")).click();
        findElementWithoutAssert(By.id("com.ttech.android.onlineislem:id/buttonPositive")).click();
        waitBySecond(5);
        existClickByKey("ızınVer");

    }


    @Step("Yeni şifre <text> ve yeni şifre tekrar <textrepeat>  alanlarına tex değerlerini yaz")
    public void writeNewPassword(String text, String textrepeat) {

        newWebDriverWait(30, 1000);
        objectTextandClick(By.id("com.ttech.android.onlineislem:id/editTextPassword"), text);
        newWebDriverWait(20, 1000);
        clickBybackButton();
        newWebDriverWait(30, 1000);
        objectTextandClick(By.id("com.ttech.android.onlineislem:id/editTextPasswordRepeat"), textrepeat);
        clickBybackButton();

    }


    @Step("<StartX>,<StartY> oranlarından <EndX>,<EndY> oranlarına <times> kere swipe et")
    public void pointToPointSwipe(int startX, int startY, int endX, int endY, int count) throws InterruptedException {
        Dimension d = appiumDriver.manage().window().getSize();

        int height = d.height;
        int width = d.width;
        startX = (width * startX) / 100;
        startY = (height * startY) / 100;
        endX = (width * endX) / 100;
        endY = (height * endY) / 100;
        for (int i = 0; i < count; i++) {
            waitBySecond(1);
            TouchAction action = new TouchAction(appiumDriver);
            action.press(PointOption.point(startX, startY))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(endX, endY))
                    .release().perform();
        }


    }


    @Step("<key> elementinin hizasından sağdan sola <times> kere kaydır")
    public void swipeFromLeftToRightAligned(String key, int times) throws InterruptedException {
        Dimension d = appiumDriver.manage().window().getSize();

        int height = d.height;
        int width = d.width;
        Point elementLocation = findElementByKeyWithoutAssert(key).getLocation();
        pointToPointSwipeWithCoordinats(width - 50, elementLocation.getY(), 40, elementLocation.getY(), times);
    }

    @Step("<key> li elementi hizala ve sagdan sola kaydır <times> kere y cordinatına <number> ekle")
    public void horizontalSwipeWithElement(String key, int times, int number) throws InterruptedException {

        if (devicesPlatformAnd()) {
            Point elementLocation = findElementByKeyWithoutAssert(key).getLocation();
            logger.info("x==" + elementLocation.getX() + " y==" + elementLocation.getY() + "----------");

            pointToPointSwipeWithCoordinats(900, elementLocation.getY(), 40, elementLocation.getY() + number, times);
            logger.info("-----horizonal kaydırma işlemi tamamlandı-----");
        } else {
            Point elementLocation = findElementByKeyWithoutAssert(key).getLocation();
            logger.info("x==" + elementLocation.getX() + " y==" + elementLocation.getY() + "----------");

            pointToPointSwipeWithCoordinats(330, elementLocation.getY(), 40, elementLocation.getY() + number, times);
            logger.info("-----horizonal kaydırma işlemi tamamlandı-----");
        }
    }

    @Step("<StartX>,<StartY> coordinatından <EndX>,<EndY> coordinatına <times> kere swipe et")
    public void pointToPointSwipeWithCoordinats(int startX, int startY, int endX, int endY, int count) throws InterruptedException {
        Dimension d = appiumDriver.manage().window().getSize();


        for (int i = 0; i < count; i++) {
            waitBySecond(3);
            TouchAction action = new TouchAction(appiumDriver);
            action.press(PointOption.point(startX, startY))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(endX, endY))
                    .release().perform();
        }


    }

    public void pointToPointSwipeForDayAndYear(int startX, int startY, int endX, int endY, int count) throws InterruptedException {
        Dimension d = appiumDriver.manage().window().getSize();
        int height = d.height;
        int width = d.width;
        if (count > 200) {
            startX = (width * startX) / 100;
            startY = (height * startY) / 100;
            endX = (width * endX) / 100;
            endY = (height * endY) / 100;
            count = count - 2020;

        } else
            count--;
        for (int i = 0; i < count; i++) {
            waitBySecond(1);
            TouchAction action = new TouchAction(appiumDriver);
            action.press(PointOption.point(startX, startY))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(endX, endY))
                    .release().perform();
        }
    }

    @Step("uygulamayı yeniden başlat")
    public void restart() throws InterruptedException {


        appiumDriver.closeApp();
        appiumDriver.launchApp();
        logger.info("uygulama yeniden başlatıldı");
        waitBySecond(5);
        existClickByKey("ızınVer");

    }


    @Step("Galeriden fotograf seç")
    public void selectPhotoFromGallery() throws InterruptedException {

        String deviceName = getCapability("deviceName");

        System.out.println("----- CİHAZDANDAN GELEN DEVİCE NAME: (" + deviceName + ")-------");
        if (deviceName.contains("CB512EHLX6")) {
            logger.info("SONY telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            clickByKey("sonyPhoto");
            existClickByKey("sonyPhotoStep2");
        } else if (deviceName.contains("EALNJVGEVODUBQ45")) {
            logger.info("General Mobile telefonu galerisine girdi");
            waitBySecond(5);
            clickByKey("samsungGallery");
            waitBySecond(5);
            existClickByKey("samsungJ5Photo");
        } else if (deviceName.contains("9889db324d434f4637")) {
            logger.info("Samsung S8 galerisine girdi");
            // existClickByKey("samsungChoose");
            //existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("5200fbe7f4688403")) {
            logger.info("Samsung A5 telefonu galerisine girdi");
            // existClickByKey("samsungChoose");
            // existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("ad051602404b854bca")) {
            logger.info("Samsung S7 Edge telefonu galerisine girdi");
            //existClickByKey("samsungChoose");
            //existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");

        } else if (deviceName.contains("ce03171382675e0f01")) {
            logger.info("Galaxy s8 (7.0) telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            //clickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("41001580c8a3a197")) {
            logger.info("Samsung Galaxy Note 4 telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("3300ee33d8728319")) {
            logger.info("Samsung Galaxy J7Primee telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("bdc156de")) {
            logger.info("Samsung Galaxy J5 telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            // existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("92010365cc6e932d")) {
            logger.info("Samsung Galaxy J2 telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("FA6A70302642")) {
            logger.info("Google Pixel 10 telefonu galerisine girdi");
            existClickByKey("googlePhotoPopupIzınver");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            // existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("R58M40CLSFJ")) {
            logger.info("Samsung Galaxy J5 telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            existClickByKey("samsungChoose");
            existClickByKey("samsungGalleryPhoto");
            existClickByKey("samsungPhoto");
        } else if (deviceName.contains("1015faa2053c3c05")) {
            logger.info("Samsung Galaxy s6(5.1.1) telefonu galerisine girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            tapByCoordinates(75, 20);
            waitBySecond(2);
            clickByKey("samsung1015Fotosecimi");


        } else {
            logger.info("iphone galeriye girdi");
            existClickByKey("ızınVer");
            waitBySecond(5);
            clickByKey("ıphoneGaleri");
            existClickByKey("ızınVer");
            existClickByKey("ıphoneGaleriPhotoChoose");
            existClickByKey("ıphoneGaleriPhotoChoose");
        }

    }

    @Step("pop-up izin ver")
    public void closePopupAndCookie() throws InterruptedException {
        waitBySecond(2);

        contextText("NATIVE_APP");

        new WebDriverWait(appiumDriver, 30).until(ExpectedConditions.presenceOfElementLocated(By.xpath("//*[@text='İZİN VER']")));

        if (isElementPresent(By.xpath("//*[@text='İZİN VER']"))
        ) {
            logger.info("Notification pop-up kapatıldı !!!!!!");
            waitBySecond(2);
            contextText("NATIVE_APP");
            findElementWithoutAssert(By.xpath("//*[@text='İZİN VER']")).click();


        } else {

            logger.info("Pop-up görülmedi");

        }


    }


    @Step("5S için <key> elementini bulana kadar yukarı kaydır")
    public void swipeFor5S(String element) {

        logger.info(" // BROWSERNAME: " + getCapability("deviceName") + " //");


        if (getCapability("deviceName").contains("5S")) {
            logger.info("5S için if koşulları gerçekleştiriliyor...");
            int maxRetryCount = 10;
            while (maxRetryCount > 0) {
                List<MobileElement> elements = findElemenstByKey(element);
                if (elements.size() > 0) {
                    if (!elements.get(0).isDisplayed()) {
                        maxRetryCount--;
                        swipeUpAccordingToPhoneSize();
                    } else {
                        elements.get(0).click();
                        logger.info(element + " elementine tıklandı");
                        break;
                    }
                } else {
                    maxRetryCount--;
                    swipeUpAccordingToPhoneSize();
                }
            }
        }

    }

    @Step("deneme checkbox")
    public void denemeCheckbox() {
        if (appiumDriver instanceof AndroidDriver) {


            contextText("WEBVIEW");
            findElementsWithoutAssert(By.cssSelector("label>i")).get(0).click();
            contextText("NATIVE_APP");

        } else {
            // findElementWithoutAssert(By.xpath("//XCUIElementTypeStaticText[@name='okudum kabul ediyorum.']")).click();
            findElementWithoutAssert(By.xpath("//XCUIElementTypeStaticText[contains(@name,'okudum')]")).click();


            System.out.println(appiumDriver.getContextHandles().toString());
            contextText("WEBVIEW");
            System.out.println(appiumDriver.getPageSource());
            contextText("NATIVE_APP");


        }

    }


    @Step("Debug step")
    public void debugStep() {

        logger.info("debug");
    }

    private void newWebDriverWait(int sec, int mil) {
        new WebDriverWait(appiumDriver, sec, mil);
    }


    private void backPage() {
        appiumDriver.navigate().back();
    }


    private void objectTextandClick(By by, String text) {
        MobileElement me = (MobileElement) appiumFluentWait.until(ExpectedConditions.presenceOfElementLocated(by));
        me.click();
        me.setValue(text);

    }

    private void contextText(String text) {

        appiumDriver.context(
                appiumDriver.getContextHandles()
                        .stream()
                        .filter(s -> s.contains(text))
                        .findFirst()
                        .get());
    }

    private String getCapability(String text) {
        return appiumDriver.getCapabilities().getCapability(text).toString();

    }

    public boolean doesElementExistByKey(String key, int time) {
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        try {
            WebDriverWait elementExist = new WebDriverWait(appiumDriver, time);
            elementExist.until(ExpectedConditions.visibilityOfElementLocated(selectorInfo.getBy()));
            return true;
        } catch (Exception e) {
            logger.info(key + " aranan elementi bulamadı");
            return false;
        }

    }

    @Step("<key>,<startPointX>,<finishPointX> kaydır baakalım")
    public void sliderSwipe(String key, int startPointX, int finishPointX) {

        int coordinateX = appiumDriver.manage().window().getSize().width;
        int pointY = findElementByKey(key).getCenter().y;
        int firstPointX = (coordinateX * startPointX) / 100;
        int lastPointX = (coordinateX * finishPointX) / 100;

        TouchAction action = new TouchAction(appiumDriver);
        action
                .press(PointOption.point(firstPointX, pointY))
                .waitAction(WaitOptions.waitOptions(ofMillis(2000)))
                .moveTo(PointOption.point(lastPointX, pointY))
                .release().perform();

    }


    public void tapElementWithCoordinate(int x, int y) {
        TouchAction a2 = new TouchAction(appiumDriver);
        a2.tap(PointOption.point(x, y)).perform();
    }

    @Step("<key> li elementin  merkezine tıkla ")
    public void tapElementWithKey(String key) {

        Point point = findElementByKey(key).getCenter();
        TouchAction a2 = new TouchAction(appiumDriver);
        a2.tap(PointOption.point(point.x, point.y)).perform();
    }

    @Step("<key> li element varsa  <x> <y> koordinatına tıkla")
    public void tapElementWithKeyCoordinate(String key, int x, int y) {

        logger.info("element varsa verilen koordinata tıkla ya girdi");
        MobileElement mobileElement;

        mobileElement = findElementByKeyWithoutAssert(key);

        if (mobileElement != null) {

            System.out.println("pakachu");
            Point point = mobileElement.getLocation();
            logger.info(point.x + "  " + point.y);
            Dimension dimension = mobileElement.getSize();
            logger.info(dimension.width + "  " + dimension.height);
            TouchAction a2 = new TouchAction(appiumDriver);
            a2.tap(PointOption.point(point.x + (dimension.width * x) / 100, point.y + (dimension.height * y) / 100)).perform();
        }
    }

    @Step("<key> li elementin  merkezine  press ile çift tıkla ")
    public void pressElementWithKey(String key) {

        Point point = findElementByKey(key).getCenter();
        TouchAction a2 = new TouchAction(appiumDriver);
        a2.press(PointOption.point(point.x, point.y)).waitAction(WaitOptions.waitOptions(Duration.ofMillis(300)))
                .press(PointOption.point(point.x, point.y)).release().perform();

    }


    @Step("<key> li elementin  merkezine double tıkla ")
    public void pressElementWithKey2(String key) {
        Actions actions = new Actions(appiumDriver);
        actions.moveToElement(findElementByKey(key));
        actions.doubleClick();
        actions.perform();
        appiumDriver.getKeyboard();

    }

    @Step("<key> li elementi rasgele sec")
    public void chooseRandomProduct(String key) {

        List<MobileElement> productList = new ArrayList<>();
        List<MobileElement> elements = findElemenstByKey(key);
        int elementsSize = elements.size();
        int height = appiumDriver.manage().window().getSize().height;
        for (int i = 0; i < elementsSize; i++) {
            MobileElement element = elements.get(i);
            int y = element.getCenter().getY();
            if (y > 0 && y < (height - 100)) {
                productList.add(element);
            }
        }
        Random random = new Random();
        int randomNumber = random.nextInt(productList.size());
        productList.get(randomNumber).click();
    }


    @Step("<key> li elemente kadar <text> textine sahip değilse ve <timeout> saniyede bulamazsa swipe yappp")
    public void swipeAndFindwithKey(String key, String text, int timeout) {


        MobileElement sktYil1 = null;
        SelectorInfo selectorInfo = selector.getSelectorInfo(key);
        WebDriverWait wait = new WebDriverWait(appiumDriver, timeout);
        int count = 0;
        while (true) {
            count++;
            try {
                sktYil1 = (MobileElement) wait.until(ExpectedConditions.visibilityOfElementLocated(selectorInfo.getBy()));
                if (text.equals("") || sktYil1.getText().trim().equals(text)) {
                    break;
                }
            } catch (Exception e) {
                logger.info("Bulamadı");

            }
            if (count == 8) {

                Assert.fail("Element bulunamadı");
            }

            Dimension dimension = appiumDriver.manage().window().getSize();
            int startX1 = dimension.width / 2;
            int startY1 = (dimension.height * 75) / 100;
            int secondX1 = dimension.width / 2;
            int secondY1 = (dimension.height * 30) / 100;

            TouchAction action2 = new TouchAction(appiumDriver);

            action2
                    .press(PointOption.point(startX1, startY1))
                    .waitAction(WaitOptions.waitOptions(ofMillis(2000)))
                    .moveTo(PointOption.point(secondX1, secondY1))
                    .release()
                    .perform();

            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

    }


    @Step("<key>li elementi bulana kadar <limit> kere swipe yap ve elementi bul")
    public void swipeKeyy(String key, int limit) throws InterruptedException {

        boolean isAppear = false;

        int windowHeight = this.getScreenHeight();
        for (int i = 0; i < limit; ++i) {
            try {

                Dimension phoneSize = appiumDriver.manage().window().getSize();
                Point elementLocation = findElementByKeyWithoutAssert(key).getLocation();
                logger.info(elementLocation.x + "  " + elementLocation.y);
                Dimension elementDimension = findElementByKeyWithoutAssert(key).getSize();
                logger.info(elementDimension.width + "  " + elementDimension.height);
                // logger.info(appiumDriver.getPageSource());
                if ((20 < elementLocation.y) && (elementLocation.y <= phoneSize.height - 30)) {
                    isAppear = true;
                    logger.info("aranan elementi buldu");
                    isAppear = true;
                    break;

                }
            } catch (Exception e) {
                System.out.println("Element ekranda görülmedi. Tekrar swipe ediliyor");
            }
            System.out.println("Element ekranda görülmedi. Tekrar swipe ediliyor");

            swipeUpAccordingToPhoneSize();
            waitBySecond(8);
        }
        if (!isAppear) {
            Assert.fail(key + " elementi bulunamadı");
        }

    }

    @Step("Tablet stokta var mi kontrol et")
    public void tabletStokKontrol() throws Exception {

        logger.info("Tablet Stok kontrolüne girdi");


        MobileElement element;
        element = findElementByKeyWithoutAssert("haberdarEt");
        waitBySecond(5);

        if (!localAndroid) {
            logger.info("ios cihaza girdi");
            if (element != null) {
                clickByKey("geriIOS");
                waitBySecond(2);
                swipeUpAccordingToPhoneSize();
                waitBySecond(5);
                selectRandomProduct("tabletSec");
            }
        } else {
            logger.info("android cihaza girdi");
            if (element != null) {
                clickByKey("geriAND");
                waitBySecond(2);
                swipeUpAccordingToPhoneSize();
                swipeUpAccordingToPhoneSize();
                waitBySecond(5);
                selectRandomProduct("tabletSec");
            }
        }

        logger.info("tablet stokta bulunuyor");
    }

    @Step("Apple için filtrele")
    public void stokCheck() throws InterruptedException {
        waitBySecond(5);
        clickByKey("filtreBtn");
        clickByKey("markalarBtn");
        clickByKey("AppleBar");
        clickByKey("uygulaBtn");


    }

    @Step("Urun stokta var mi kontrol et ikinci sıra= <key1> birinci element = <key2>")
    public void stokKontrol(String key1, String key2) throws Exception {
        int i = 0;

        logger.info("Telefon Stok kontrolüne girdi");
        MobileElement element;
        waitBySecond(6);

        swipeUpAccordingToPhoneSize();
        element = findElementByKeyWithoutAssert("haberdarEt");
        while (element != null && i < 6) {
            i++;
            //clickBybackButton();
            clickByKey("geriBtn");
            waitBySecond(2);
            swipeUpAccordingToPhoneSize();
            waitBySecond(5);
            firstElementClickOtherwiseSecentClick(key1, key2);
            waitBySecond(8);
            swipeUpAccordingToPhoneSize();
            element = null;
            element = findElementByKeyWithoutAssert("haberdarEt");

        }
        logger.info("telefon stokta bulunuyor");

    }

    public void firstElementClickOtherwiseSecentClick(String key1, String key2) throws InterruptedException {
        MobileElement element;
        element = findElementByKeyWithoutAssert(key1);
        waitBySecond(3);
        if (element != null) {
            clickByKey(key1);
        } else {
            clickByKey(key2);
        }


    }

    @Step("Aksesuar stokta var mi kontrol et")
    public void aksesuarStokKontrol() throws Exception {

        logger.info("Aksesuar Stok kontrolüne girdi");


        MobileElement element;
        element = findElementByKeyWithoutAssert("haberdarEt");
        waitBySecond(5);

        if (!localAndroid) {
            logger.info("ios cihaza girdi");
            if (element != null) {

                clickByKey("geriIOS");
                waitBySecond(2);
                swipeUpAccordingToPhoneSize();
                waitBySecond(5);
                selectRandomProduct("AksesuarSec");

            }
        } else {
            logger.info("android cihaza girdi");
            if (element != null) {

                clickByKey("geriAND");
                waitBySecond(2);
                swipeUpAccordingToPhoneSize();
                swipeUpAccordingToPhoneSize();
                waitBySecond(5);
                selectRandomProduct("AksesuarSec");

            }
        }

        logger.info("aksesuar stokta bulunuyor");

    }

    @Step("<key> üründen Random  sec ")
    public void selectRandomProduct(String key) {

        logger.info("Random ürün seçimine girdi");

        SelectorInfo selectorInfo = selector.getSelectorInfo(key);


        List<MobileElement> element = findElementsWithAssert(selectorInfo.getBy());

        MobileElement randomProduct = element.get(new Random().nextInt(element.size()));

        logger.info("Random elemente tıkladı ");

        randomProduct.click();

    }

    @Step("<key> elementi bulunmuyorsa <errorKey> varsa <warning> uyarısı verilir")
    public void errorControl(String key, String errorKey, String warning) throws InterruptedException {
        SelectorInfo selectorInfo;
        FluentWait<AppiumDriver> fluentWait = new FluentWait<AppiumDriver>(appiumDriver)
                .withTimeout(Duration.ofSeconds(30))
                .pollingEvery(Duration.ofMillis(300))
                .ignoring(NoSuchElementException.class);
        try {

            selectorInfo = selector.getSelectorInfo(key);
            fluentWait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(selectorInfo.getBy()));
        } catch (Exception e) {
            if (errorKey.equals("")) {
                throw new SessionNotCreatedException("Sayfa Yüklenemedi");
            }
            selectorInfo = selector.getSelectorInfo(errorKey);

            // if (appiumDriver.findElements(selectorInfo.getBy()).size() > 0) {
            waitBySecond(3);
            try {
                fluentWait.withTimeout(Duration.ofSeconds(6)).until(ExpectedConditions.presenceOfAllElementsLocatedBy(selectorInfo.getBy()));
            } catch (Exception e2) {
                throw new SessionNotCreatedException("Sayfa Yüklenemedi");
            }
            throw new SessionNotCreatedException(warning);
        }

    }
    @Step("<talepKey> talebine gir ve talepte bulun <warningKey> uyarısı hata vermeden devam et")
    public void talepIletWithOuthError(String talepKey, String warningKey){
        findElementByKey("talepKey").click();
        if(doesElementExistByKey(warningKey,10)){

            return;
        }
    }


    @Step("<key> elementi sayfada yer almıyor <errorKey> yer alıyorsa <warning> mesajı verilir")
    public void warningControl(String key, String errorKey, String warning) {
        SelectorInfo selectorInfo;
        FluentWait<AppiumDriver> fluentWait = new FluentWait<AppiumDriver>(appiumDriver)
                .withTimeout(Duration.ofSeconds(30))
                .pollingEvery(Duration.ofMillis(300))
                .ignoring(NoSuchElementException.class);
        try {
            selectorInfo = selector.getSelectorInfo(key);
            fluentWait.until(ExpectedConditions.presenceOfAllElementsLocatedBy(selectorInfo.getBy()));
        } catch (Exception e) {
            if (errorKey.equals("")) {
                throw new SessionNotCreatedException("Sayfa Yüklenemedi");
            }
            selectorInfo = selector.getSelectorInfo(errorKey);
            // if (appiumDriver.findElements(selectorInfo.getBy()).size() > 0) {
            try {
                fluentWait.withTimeout(Duration.ofSeconds(6)).until(ExpectedConditions.presenceOfAllElementsLocatedBy(selectorInfo.getBy()));
            } catch (Exception e2) {
                throw new SessionNotCreatedException(warning);
            }
        }
    }

    @Step("<key> li  telefonun  <x> ve elementin <y> kordinatına göre tıkla")
    public void elementFindwithXandYcoordinate(String key, int x, int y) {

        WebElement element = findElementByKey(key);
        int height = element.getLocation().y + (element.getSize().height * y) / 100;
        int width = (appiumDriver.manage().window().getSize().width * x) / 100;
        System.out.println(height + "  " + width + "   ");
        TouchAction action = new TouchAction(appiumDriver);
        action.tap(PointOption.point(width, height)).perform();


    }

    @Step("Sepeti boşalt")
    public void clearBasket() throws Exception {
        clickByKey("magazaButonu");
        clickByKey("SepetinMagaza");
        MobileElement mobileElement = null;

        System.out.println("Sepeti Sil'e girdi");
        while (true) {
            try {

                doesElementExistByKey("SepettenSilBtn", 5);
                SelectorInfo selectorInfo = selector.getSelectorInfo("SepettenSilBtn");
                mobileElement = selectorInfo.getIndex() > 0 ? findElements(selectorInfo.getBy())
                        .get(selectorInfo.getIndex()) : findElement(selectorInfo.getBy());
                mobileElement.click();
                mobileElement = null;
                doesElementExistByKey("sepetimSilEvet", 5);
                selectorInfo = selector.getSelectorInfo("sepetimSilEvet");
                mobileElement = selectorInfo.getIndex() > 0 ? findElements(selectorInfo.getBy())
                        .get(selectorInfo.getIndex()) : findElement(selectorInfo.getBy());
                mobileElement.click();


//                findElementByKey("SepettenSilBtn").click();
//                findElementByKey("sepetimSilEvet").click();
            } catch (Exception e) {
                System.out.println(" Sepet Temizlendi");
                break;
            }
        }
        clickByKey("carpıButonIkı");
    }


    @Step("kayıtlı kart varsa odeme yap")
    public void registeredCard() throws InterruptedException {

        if (!localAndroid) {
            System.out.println("ios cihazda kayıtlı kart kontrolune girdi");

            MobileElement element = findElementWithoutAssert(By.xpath("//XCUIElementTypeStaticText[@name=\"Kayıtlı Kartlarınız\"]"));

            if (element != null) {
                textWrite("faturaTalımatAdi", 5, 25, "Test");
                // sendKeysByKeyNotClear("faturaTalımatAdi", "Test Ödeme Talimatı");
                existClickByKey("toolbarDoneButton");
                //sendKeysByKeyNotClear("faturaGuvenlıkKodu", "458");
                textWrite("faturaGuvenlıkKodu", 5, 5, "458");
                existClickByKey("toolbarDoneButton");

            } else {

                elementFindwithXandYcoordinate("farkliKredıKartiOtoOdeme", 30, 50);
                pointToPointSwipe(50, 60, 50, 30, 1);
                sendKeysByKeyNotClear("talımatAdiFarkliKart", "Test Otomatik Ödeme");
                appiumDriver.findElement(By.xpath("//XCUIElementTypeButton[@name='Bitti']")).click();
                sendKeysByKeyNotClear("adsoyadFarkliKart", "Turkcell Test");
                appiumDriver.findElement(By.xpath("//XCUIElementTypeButton[@name='Bitti']")).click();
                sendKeysByKeyNotClear("kartnumarasiFarkliKart", "5440786728974016");
                appiumDriver.findElement(By.xpath("//XCUIElementTypeButton[@name='Bitti']")).click();
                pointToPointSwipe(50, 60, 50, 30, 1);


                elementFindwithXandYcoordinate("aysecımıFarkliKart", 85, 50);
                sendKeysByKeyNotClear("sonKullanmaTarihi-Ay", "5");
                appiumDriver.findElement(By.xpath("//XCUIElementTypeButton[@name='Bitti']")).click();
                elementFindwithXandYcoordinate("yilsecımıFarkliKart", 85, 50);
                sendKeysByKeyNotClear("sonKullanmaTarihi-Yıl", "2021");
                appiumDriver.findElement(By.xpath("//XCUIElementTypeButton[@name='Bitti']")).click();
                sendKeysByKey("cvvAlaniFarkliKart", "936");
                appiumDriver.findElement(By.xpath("//XCUIElementTypeButton[@name='Bitti']")).click();

            }

        }
    }


    @Step("elementsiz alana text <text> yazdir")
    public void sendKeysKeyCode(String keyCode) {

        ((AndroidDriver) appiumDriver).pressKey(new KeyEvent().withKey(AndroidKey.valueOf(keyCode)));
    }

    @Step("elementsiz alana sayıyı <sayıyı> yazdir")
    public void sendKeysKeyCodeAsNumPad(String keyCode) {

        AndroidDriver androidDriver = (AndroidDriver) appiumDriver;
        char[] charList = keyCode.toCharArray();
        for (int i = 0; i < charList.length; i++) {
            androidDriver.pressKey(new KeyEvent().withKey(AndroidKey.valueOf("NUMPAD_" + charList[i])));
        }
    }

    @Step("elementsiz alana  sayıyı <sayıyı> yazdir bakalim")
    public void sendKeysKeyCodeAsDIGIT(String keyCode) {

        AndroidDriver androidDriver = (AndroidDriver) appiumDriver;
        char[] charList = keyCode.toCharArray();
        for (int i = 0; i < charList.length; i++) {
            androidDriver.pressKey(new KeyEvent().withKey(AndroidKey.valueOf("DIGIT_" + charList[i])));
        }
    }

    @Step("<key> elementinin koordinatlarına x=<x> y=<y> degerlerini ekleyerek 2 kere tıkla")
    public void coordinatDoubleClickWithAdds(String key, int x, int y) throws InterruptedException {
        waitBySecond(3);
        MobileElement me = findElementByKey(key);
        tapElementWithCoordinate(me.getLocation().x + x, me.getLocation().y + y);
        tapElementWithCoordinate(me.getLocation().x + x, me.getLocation().y + y);
        tapElementWithCoordinate(me.getLocation().x + x, me.getLocation().y + y);


    }

    @Step("<key> elementinin koordinatlarına x=<x> y=<y> degerlerini ekleyerek tıkla")
    public void coordinatClickWithAdds(String key, int x, int y) throws InterruptedException {
        waitBySecond(3);
        MobileElement me = findElementByKey(key);
        tapElementWithCoordinate(me.getLocation().x + x, me.getLocation().y + y);

    }

    @Step("paket bitimi tarihi kontrolü yap hata alırsan <warning> mesajını göster")
    public void dateCheck(String warning) throws ParseException {
        LocalDate date = LocalDate.now();
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd");
        String yenilemeTarihi;
        String leftDay;

        if (localAndroid) {
            yenilemeTarihi = findElementByKey("yenilemeBitiş").getText();
            leftDay = findElementByKey("kalanGünSayısı").getText();
        } else {
            yenilemeTarihi = findElementByKey("yenilemeBitiş").getAttribute("name");
            leftDay = findElementByKey("kalanGünSayısı").getAttribute("name");
        }

        leftDay = leftDay.substring(0, 2);
        yenilemeTarihi = yenilemeTarihi.substring(15, 17);
        int trimedleftDay = NumberFormat.getInstance().parse(leftDay).intValue();
        int trimedyenilemeTarihi = NumberFormat.getInstance().parse(yenilemeTarihi).intValue();
        if (trimedyenilemeTarihi - Integer.valueOf(date.format(formatter)) == trimedleftDay) {
            logger.info("Kalan gün sayısı dogrulugu onaylandı");
        } else {
            throw new SessionNotCreatedException(warning);

        }


    }

    @Step("kredi kartı son kulanma tarihi gir <ay> / <yil>")
    public void phoneSize(int ay, int yil) throws InterruptedException {

        String deviceName = getCapability("deviceName");

        System.out.println("----- CİHAZDANDAN GELEN DEVİCE NAME: (" + deviceName + ")-------");
        if (deviceName.contains("CB512EHLX6")) {

            logger.info("SONY telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(355, 1359, 355, 1637, 9);
            pointToPointSwipeForDayAndYear(355, 1526, 355, 1462, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("EALNJVGEVODUBQ45")) {
            logger.info("General Mobile telefonu swipe degerleri alındı");

        } else if (deviceName.contains("9889db324d434f4637")) {
            logger.info("Samsung S8 telefonu swipe degerleri alındı");

        } else if (deviceName.contains("5200fbe7f4688403")) {
            logger.info("Samsung A5 telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(333, 1475, 333, 1754, 9);
            pointToPointSwipeForDayAndYear(333, 1652, 333, 1591, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("ad051602404b854bca")) {
            logger.info("Samsung S7 Edge telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(325, 1703, 325, 1880, 12);
            pointToPointSwipeForDayAndYear(352, 1692, 352, 1603, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);


        } else if (deviceName.contains("ce03171382675e0f01")) {
            logger.info("Galaxy s8 (7.0) telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(343, 1795, 319, 2079, 5);
            pointToPointSwipeForDayAndYear(339, 1959, 339, 1879, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("41001580c8a3a197")) {
            logger.info("Samsung Galaxy Note 4 telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(449, 1940, 449, 2344, 6);
            pointToPointSwipeForDayAndYear(449, 2250, 449, 2147, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("1015faa2053c3c05")) {
            logger.info("Samsung Galaxy Note 4 telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(449, 1960, 449, 2354, 5);
            pointToPointSwipeForDayAndYear(449, 2266, 449, 2182, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("3300ee33d8728319")) {
            logger.info("Samsung Galaxy J7Primee telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(337, 1483, 337, 1800, 5);
            pointToPointSwipeForDayAndYear(337, 1712, 337, 1640, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("bdc156de")) {
            logger.info("Samsung Galaxy J5 telefonu swipe degerleri alındı");

        } else if (deviceName.contains("92010365cc6e932d")) {
            logger.info("Samsung Galaxy J2 telefonu swipe degerleri alındı");

        } else if (deviceName.contains("FA6A70302642")) {
            logger.info("Google Pixel 10 telefonu swipe degerleri alındı");
            pointToPointSwipeForDayAndYear(341, 1390, 341, 1680, 5);
            pointToPointSwipeForDayAndYear(319, 1579, 319, 1494, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("R58M40CLSFJ")) {
            logger.info("Samsung Galaxy J5 telefonu swipe degerleri alındı");

            pointToPointSwipeForDayAndYear(337, 1483, 337, 1800, 5);
            pointToPointSwipeForDayAndYear(319, 2059, 319, 2025, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else if (deviceName.contains("eda14cff")) {
            logger.info("Samsung Galaxy J5 telefonu swipe degerleri alındı");

            pointToPointSwipeForDayAndYear(337, 1483, 337, 1800, 5);
            pointToPointSwipeForDayAndYear(319, 2059, 319, 2025, ay);
            pointToPointSwipeForDayAndYear(75, 90, 75, 85, yil);

        } else {
            sendKeysByKeyNotClear("sonKullanmaTarihi-Ay", String.valueOf(ay));
            sendKeysByKeyNotClear("sonKullanmaTarihi-Yıl", String.valueOf(yil));
            logger.info("iphone telefonu swipe degerleri alındı");

        }

    }

    // @Step("Select birhdate ios <key> day: <day> year: <year>")
    public void selectBirthdateIossdd(String key, String day, String year) throws InterruptedException {
        clickByKey(key);
        appiumDriver.findElementsByClassName("XCUIElementTypePickerWheel").get(0).setValue(day);
        appiumDriver.findElementsByXPath("//*[@resource-id='com.ttech.android.onlineislem:id/editTextExpires']").get(0).setValue("3");
        //bunu sayı olarak ver
        //appiumDriver.findElementsByClassName("XCUIElementTypePickerWheel").get(1).setValue("August");
        appiumDriver.findElementsByClassName("XCUIElementTypePickerWheel").get(2).setValue(year);
        appiumDriver.findElement(MobileBy.AccessibilityId("Done")).click();
    }

    @Step("Select birhdate ios <key> day: <day> year: <year>")
    public void selectBirthdateIos(String key, String day, String year) throws Exception {
        clickByKey(key);
        MobileElement element = findElement(By.xpath("//*[@resource-id='com.ttech.android.onlineislem:id/editTextExpires']"));
        ;
        waitBySecond(4000);
        appiumDriver.findElementsByClassName("android.view.View").get(0).setValue(day);
        appiumDriver.findElementsByClassName("android.view.View").get(1).setValue(year);

    }

    @Step("bildirimleri sil")
    public void deleteNotifications() throws InterruptedException {
        List<MobileElement> barisList;
        int startx, endx, y;
        if (localAndroid) {
            barisList = appiumDriver.findElements(By.xpath("//*[@resource-id='com.ttech.android.onlineislem:id/recyclerView']/*[1]"));
            startx = 800;
            endx = 400;
            y = 9;
        } else {
            barisList = appiumDriver.findElements(By.xpath("(//*[@type='XCUIElementTypeCell'][1])[2]"));
            startx = 300;
            endx = 200;
            y = 9;
        }

        while (barisList.size() > 0) {
            Point point = findElementByKey("ilkBildirim").getLocation();
            System.out.println(point.getY() + "d----------------------------- ");
            pointToPointSwipeWithCoordinats(startx, point.getY() + y, endx, point.getY() + y, 1);
            waitBySecond(3);
            findElementByKey("SilBtn").click();
            waitBySecond(3);

            if (localAndroid) {
                barisList = appiumDriver.findElements(By.xpath("//*[@resource-id='com.ttech.android.onlineislem:id/recyclerView']/*[1]"));
            } else {
                barisList = appiumDriver.findElements(By.xpath("(//*[@type='XCUIElementTypeCell'][1])[2]"));
            }
        }
    }

    @Step("mesajlarım tarih sıralaması kontrolu")
    public void messageDateControl() throws InterruptedException {
        waitBySecond(21);

        for (int i = 1; i < 6; i++) {
            String date1 = appiumDriver.findElementByXPath("(//*[@resource-id='com.ttech.android.onlineislem:id/textViewDate'])[" + i + "]").getText();
            String date2 = appiumDriver.findElementByXPath("(//*[@resource-id='com.ttech.android.onlineislem:id/textViewDate'])[" + (i + 1) + "]").getText();
            String mounth1 = date1.replaceAll("[^A-Z]", "");
            String mounth2 = date2.replaceAll("[^A-Z]", "");
            date1 = date1.substring(0, 2);
            date2 = date2.substring(0, 2);
            date1 = date1.replace(" ", "");
            date2 = date2.replace(" ", "");
            int date11 = Integer.parseInt(date1);
            int date22 = Integer.parseInt(date2);
            System.out.println(mounth1 + "  " + mounth2);
            if (mounth1.equals(mounth2)) {
                if (date11 < date22)
                    Assert.fail("Mesajlarda Tarih Sıralaması Yanlış");
            }
            System.out.println(i + ". tarih doğru");

        }
    }


    @Step("<x>,<y> koordinatlarına tıkla")
    public void koordinataTikla(int x, int y) {
        TouchAction a2 = new TouchAction(appiumDriver);
        a2.tap(PointOption.point(x, y)).perform();
        logger.info("tıklama yapıldı");
    }

    @Step("<text> ile giriş yapılmamıssa giriş yap android şifre=<password>")
    public void loginİfNot(String text, String password) throws InterruptedException {
        existClickByKey("ızınVer");
        existClickByKey("googlePıxelreddetBtn");
        existClickByKey("googlePıxelIzınverBtn");
        waitBySecond(4);
        //waitBySecond(10);
        if (doesElementExistByKey("anasayfaGirisYapButonu", 10)) {
            getLogin(text, password);
        } else {
            if (findElementByKey("numaram").getText().equals(text)) {
                logger.info("İstenen numara halihazırda login");
            } else {
                LoginControl();
                waitBySecond(5);
                getLogin(text, password);
            }
        }
    }

    public void getLogin(String text, String password) throws InterruptedException {
        clickByKey("anasayfaGirisYapButonu");
        waitBySecond(2);
        sendKeysByKeyNotClear("gsmNumarasıalanı", text);
        hideAndroidKeyboard();
        if (senarioName.contains("Beni Unut")) {
            clickByKey("rememberMeChckbox");
        }
        clickByKey("loginDevambutonu");
        waitBySecond(2);
        clickByKey("sifreileGirisyapButonu");
        sendKeysByKeyNotClear("sifreGirisalanı", password);
        hideAndroidKeyboard();
        clickLoginButton();
        waitBySecond(5);
        getPageSourceFindWord(text);
    }

    public void getNonLogin(String text, String password) throws InterruptedException {
        clickByKey("anasayfaGirisYapButonu");
        waitBySecond(2);
        sendKeysByKeyNotClear("gsmNumarasıalanı", text);
        hideAndroidKeyboard();
        clickByKey("loginDevambutonu");
        waitBySecond(2);
        //clickByKey("sifreileGirisyapButonu");
        sendKeysByKeyNotClear("sifreGirisalanı", password);
        hideAndroidKeyboard();
        clickLoginButton();
        waitBySecond(5);
        //getPageSourceFindWord(text);
    }

    @Step("IOS <text> numarası ve <password> şifresi ile giriş yapılmamıssa giriş yap")
    public void IOSLogin(String text, String password) throws InterruptedException {
        waitBySecond(5);
        if (!appiumDriver.getPageSource().contains(text)) {
            if (appiumDriver.getPageSource().contains("Giriş Yap")) {
                logger.info("Hiçbir hesap login değil, giriş yapılıyor");
                clickByKey("anasayfaGirisYapButonu");
                sendKeysByKeyNotClear("gsmNumarasıalanı", text);
                clickByKey("ekranadokun");
                clickByKey("loginDevambutonu");
                waitBySecond(2);
                clickByKey("sifreileGirisyapButonu");
                sendKeysByKeyNotClear("sifreGirisalanı", password);
                clickByKey("ekranadokun");
                clickByKey("girisYapButonu");
                waitBySecond(5);
            } else {
                logger.info("Başka bir hesap login halde, hesap değiştiriliyor");
                clickByKey("profilSekmesiBtn");
                waitBySecond(3);
                swipe(2);
                clickByKeyWithSwipe("profilAyarGit");
                waitBySecond(3);
                swipe(4);
                clickByKeyWithSwipe("cikisButonu");
                clickByKey("popupCikisYapButonu");
                waitBySecond(5);
                clickByKey("anasayfaGirisYapButonu");
                sendKeysByKeyNotClear("gsmNumarasıalanı", text);
                clickByKey("ekranadokun");
                clickByKey("loginDevambutonu");
                waitBySecond(2);
                clickByKey("sifreileGirisyapButonu");
                sendKeysByKeyNotClear("sifreGirisalanı", password);
                clickByKey("ekranadokun");
                clickByKey("girisYapButonu");
                waitBySecond(5);
            }
        } else {
            logger.info("İstenen numara login halde");
        }

    }


    @Step("Numara:<text> ve şifre:<password> ile giriş yapılmamışsa giriş yap")
    public void login(String text, String password) throws InterruptedException {
        if(text.contains("Faturalı")){
            text=kullanıcıBilgileri.getString("FaturalıNumara");
            password=kullanıcıBilgileri.getString("FaturalıSifre");
        } else if (text.contains("Pre")){
            text=kullanıcıBilgileri.getString("PrepaidNumara");
            password=kullanıcıBilgileri.getString("PrepaidSifre");
        }

        hideAndroidKeyboard();
        waitBySecond(5);
        if (devicesPlatformAnd()) {
            loginWithAnd(text, password);
        } else {
            loginWithIOS(text, password);
        }


    }

  @Step("izinver butonuna bas")
  public void loginWithAnd() throws InterruptedException {
      String deviceName = getCapability("deviceName");
      waitBySecond(5);
      existClickByKey("ızınVer");
      if (deviceName.contains("FA6A70302642")) {
          existClickByKey("googlePıxelreddetBtn");
          existClickByKey("googlePıxelIzınverBtn");
      }

    }

    public void loginWithAnd(String text, String password) throws InterruptedException {
        String deviceName = getCapability("deviceName");
        waitBySecond(5);
        existClickByKey("ızınVer");
        if (deviceName.contains("FA6A70302642")) {
            existClickByKey("googlePıxelreddetBtn");
            existClickByKey("googlePıxelIzınverBtn");
        }
        waitBySecond(4);

        if (doesElementExistByKey("anasayfaGirisYapButonu", 10)) {
            getLogin(text, password);
        } else {
            if (findElementByKey("numaram").getText().equals(text)) {
                logger.info("İstenen numara halihazırda login");
            } else {
                LoginControl();
                waitBySecond(5);
                getLogin(text, password);
            }
        }

    }

    public void loginWithIOS(String text, String password) throws InterruptedException {
        waitBySecond(5);
        if (!appiumDriver.getPageSource().contains(text)) {
            if (doesElementExistByKey("GirisYapText", 3)) {
                logger.info("Hiçbir hesap login değil, giriş yapılıyor");
                clickByKey("anasayfaGirisYapButonu");
                waitBySecond(4);
                sendKeysByKeyNotClear("gsmNumarasıalanı", text);
                clickByKey("ekranadokun");
                if (senarioName.contains("Beni Unut")) {
                    clickByKey("rememberMeChckbox");
                }

                clickByKey("loginDevambutonu");
                waitBySecond(2);
                if (text.equals("5054039973")) {
                    clickByKey("gecicişifrebarı");
                } else {
                    clickByKey("sifreileGirisyapButonu");
                }
                sendKeysByKeyNotClear("sifreGirisalanı", password);
                clickByKey("ekranadokun");
                clickByKey("girisYapButonu");
                waitBySecond(5);
            } else {
                logger.info("Başka bir hesap login halde, hesap değiştiriliyor");
                clickByKey("profilSekmesiBtn");
                waitBySecond(3);
                swipe(2);
                clickByKeyWithSwipe("profilAyarGit");
                waitBySecond(3);
                swipe(2);
                if(doesElementExistByKey("cikisButonu",10)){
                    clickByKeyWithSwipe("cikisButonu");
                  //  coordinatClickWithAdds("cikisButonu",3,3); //test için eklendi
                } else {
                    coordinateTap(100,805);
                }
                waitBySecond(4);
                clickByKey("popupCikisYapButonu");
                waitBySecond(5);
                clickByKey("anasayfaGirisYapButonu");
                sendKeysByKeyNotClear("gsmNumarasıalanı", text);
                clickByKey("ekranadokun");

                clickByKey("loginDevambutonu");
                waitBySecond(2);
                if (text.equals("5054039973")) {
                    clickByKey("gecicişifrebarı");
                } else {
                    clickByKey("sifreileGirisyapButonu");
                }
                sendKeysByKeyNotClear("sifreGirisalanı", password);
                clickByKey("ekranadokun");
                clickByKey("girisYapButonu");
                waitBySecond(5);
            }
        } else {
            logger.info("İstenen numara login halde");
        }
    }

    @Step("Kullanıcı girişi yapılmışsa çıkış yap")
    public void logout() throws InterruptedException {
        String deviceName = getCapability("deviceName");
        if (devicesPlatformAnd()) {
            existClickByKey("ızınVer");
            if (deviceName.contains("FA6A70302642")) {
                existClickByKey("googlePıxelreddetBtn");
                existClickByKey("googlePıxelIzınverBtn");
            }
            if (!doesElementExistByKey("anasayfaGirisYapButonu", 10)) {
                LoginControl();
            }

        } else {
            waitBySecond(5);
            if (!doesElementExistByKey("anasayfaGirisYapButonu", 3)) {
                logger.info("IOS çıkış yapılıyor");
                clickByKey("profilSekmesiBtn");
                waitBySecond(3);
                swipe(2);
                clickByKeyWithSwipe("profilAyarGit");
                waitBySecond(3);
                swipe(4);
                clickByKeyWithSwipe("cikisButonu");
                clickByKey("popupCikisYapButonu");
                waitBySecond(5);
            }

        }

        if (!doesElementExistByKey("anasayfaGirisYapButonu", 3)) {
            logger.info("Giris yap yok");
            clickByKey("profilSekmesiBtn");
            waitBySecond(3);
            swipe(2);
            clickByKeyWithSwipe("profilAyarGit");
            waitBySecond(3);
            swipe(4);
            clickByKeyWithSwipe("cikisButonu");
            clickByKey("popupCikisYapButonu");
            waitBySecond(5);
            getPageSourceFindWord("Giriş Yap");
        }
    }

    public boolean devicesPlatformAnd() {
        if (StringUtils.isEmpty(System.getenv("key"))) {
            if (localAndroid) {
                return true;
            } else {
                return false;
            }
        } else {
            if (System.getenv("platform").equals("ANDROID")) {
                return true;
            } else {
                return false;
            }
        }
    }


    @Step("Indirme ve yükleme değerlerinin toplamının toplam kullanımı verdiğini kontrol et")
    public void checkTotal() throws InterruptedException {
        swipeKeyy("superOnlineYuklemeBilgisi", 4);
        String yukleme = findElementByKey("superOnlineYuklemeBilgisi").getText();
        String[] deger = yukleme.split(" ");
        String value = deger[1];

        int number = Integer.parseInt(value);
        logger.info("Yukleme: " + number);
        String indirme = findElementByKey("superOnlineIndirmeBilgisi").getText();
        String[] deger1 = indirme.split(" ");
        String value1 = deger1[1];
        System.out.println(value1);

        int number1 =  Integer.parseInt(value1);
        logger.info("Indirme: " + number1);
        String toplam = findElementByKey("superOnlineToplamKullanimBilgisi").getText();
        String[] toplam1 = toplam.split(" ");
        String toplamasString = toplam1[0];
        int number2 =  Integer.parseInt(toplamasString);
        logger.info("Toplam: " + number2);
        Assert.assertEquals(number2, number + number1);
    }


    @Step("<key> istenilen sayfaya geçilip geçilmediği kontrol edilir")
    public WebElement checkGooglePlay(String key) throws InterruptedException {

        WebElement webElement;
        int loopCount = 0;
        while (loopCount < 200) {
            try {
                webElement = findElementByKey(key);
                //logger.info("Element:'" + key + "' found.");
                return webElement;

            } catch (WebDriverException e) {
            }
            loopCount++;
            waitBySecond(200);
        }
        Assert.fail("Element: '" + key + "'bulunamadı.");
        return null;
    }


    @Step("Non turkcell num:<user> şifre:<password> ile giriş yapılmamışsa giriş yap")
    public void NonTurkcellogin(String user, String password) throws InterruptedException {
        hideAndroidKeyboard();
        waitBySecond(5);
        if (devicesPlatformAnd()) {
            loginWithAndNon(user, password);
        } else {
            loginWithIOSNon(user, password);
        }
    }

    public void loginWithAndNon(String user, String password) throws InterruptedException {
        String deviceName = getCapability("deviceName");
        waitBySecond(5);
        existClickByKey("ızınVer");
        if (deviceName.contains("FA6A70302642")) {
            existClickByKey("googlePıxelreddetBtn");
            existClickByKey("googlePıxelIzınverBtn");
        }
        waitBySecond(4);

        if (doesElementExistByKey("anasayfaGirisYapButonu", 10)) {
            getNonLogin(user, password);
        } else {
            if (findElementByKey("numaram").getText().equals(user)) {
                logger.info("İstenen numara halihazırda login");
            } else {
                LoginControl();
                waitBySecond(5);
                getNonLogin(user, password);
            }
        }
    }


    public void loginWithIOSNon(String user, String password) throws InterruptedException {
        waitBySecond(5);
        if (!appiumDriver.getPageSource().contains(user)) {
            if (doesElementExistByKey("GirisYapText", 3)) {
                logger.info("Hiçbir hesap login değil, giriş yapılıyor");
                clickByKey("anasayfaGirisYapButonu");
                waitBySecond(4);
                sendKeysByKeyNotClear("gsmNumarasıalanı", user);
                clickByKey("ekranadokun");
                clickByKey("loginDevambutonu");
                waitBySecond(2);
                sendKeysByKeyNotClear("sifreGirisalanı", password);
                clickByKey("ekranadokun");
                clickByKey("girisYapButonu");
                waitBySecond(5);
            } else {
                logger.info("Başka bir hesap login halde, hesap değiştiriliyor");
                clickByKey("profilSekmesiBtn");
                waitBySecond(3);
                swipe(2);
                clickByKeyWithSwipe("profilAyarGit");
                waitBySecond(3);
                swipe(2);
                clickByKeyWithSwipe("cikisButonu");
                clickByKey("popupCikisYapButonu");
                waitBySecond(5);
                clickByKey("anasayfaGirisYapButonu");
                sendKeysByKeyNotClear("gsmNumarasıalanı", user);
                clickByKey("ekranadokun");
                clickByKey("loginDevambutonu");
                waitBySecond(2);
                sendKeysByKeyNotClear("sifreGirisalanı", password);
                clickByKey("ekranadokun");
                clickByKey("girisYapButonu");
                waitBySecond(5);
            }
        } else {
            logger.info("İstenen numara login halde");
        }
    }

    @Step("<key> varsa tıkla yoksa <keyKoordinat> koordinata göre tıkla")
    public void clickElementAndKoordinat(String key, String keyKoordinat) throws InterruptedException {
        if (doesElementExistByKey(key, 3)) {
            clickByKey(key);
        } else {
            coordinatClickWithAdds(keyKoordinat, -100, 400);

        }
    }

    @Step("Fatura ödeme")
    public void faturaOdeme() throws InterruptedException {
        int i = 0;
        while (i < 4) {
            i++;
            swipe(1);
            if (doesElementExistByKey("hemenOdeButonu", 3)) {
                i = 0;
                break;
            }
        }

        if (i == 0) {
            clickByKey("hemenOdeButonu");
            isElementExist("hemenÖdeKartSeçimi", "1");
            clickByKey("hemenÖdeKartSeçimi");
            sendKeysByKeyNotClear("cvvKartSeçimi", "458");
            clickByKey("hemenOdeCvv");
            existElement("kartDogrulamaSayfası");
        } else {
            logger.info("ödenmemiş fatura bulunmamaktadır");
        }


    }

    @Step("Fatura ödeme sayfasına gir ve kontro et")
    public void checkBills() throws InterruptedException {
        swipeKeyy("hemenOdeButonu", 5);
        if (doesElementExistByKey("hemenOdeButonu", 10)) {
            doesElementExistByKey("odenmemisFaturaBilgisi", 10);
            clickByKey("hemenOdeButonu");
            isNotElementExist("odenmemisFaturaBilgisi", "HEMEN ÖDE SAYFASINA GEÇİLEMEDİ");
        }
    }

    @Step("testttt")
    public void testtt() {
        appiumDriver.findElement(By.xpath("//*[@value='2002']")).setValue("1984");
    }


    public String cardInformationNo() {

        String deviceName = getCapability("deviceName");

        if (deviceName.contains("b3cff391ba9dab26e91d2166fd5ea426930c8a99")) {
            logger.info(" Telefonu için  numaralı kart bilgileri alındı");
            return "3";

        } else if (deviceName.contains("20851146c4af5d94d21f8148c4ee64bf4c83bd7d")) {
            logger.info("IPHONE 7 Telefonu için 1 numaralı kart bilgileri alındı");
            return "2";
        } else if (deviceName.contains("b12a671d4707d092ada70a55da870544c9353357")) {
            logger.info("IPHONE 8 PLUS Telefonu için 1 numaralı kart bilgileri alındı");

            return "1";
        } else if (deviceName.contains("7408c37fc1e35803aaaba22c2680c7b0254ace58")) {
            logger.info("IPHONE 6S PLUS Telefonu için  numaralı kart bilgileri alındı");

            return "3";
        } else if (deviceName.contains("ed78cdcfdb7f773d92c84fc37d318056b9baa2b1")) {
            logger.info("IPHONE X Telefonu için  numaralı kart bilgileri alındı");

            return "2";
        } else if (deviceName.contains("1015faa2053c3c05")) {
            return "1";
        } else if (deviceName.contains("b3cff391ba9dab26e91d2166fd5ea426930c8a99")) {
            logger.info("SAMSUNG GALAXY S6 Telefonu için  numaralı kart bilgileri alındı");

            return "3";
        } else if (deviceName.contains("5200fbe7f4688403")) {
            logger.info("SAMSUNG GALAXY A5 Telefonu için  numaralı kart bilgileri alındı");

            return "2";
        } else if (deviceName.contains("ad051602404b854bca")) {
            logger.info("GALAXY S7 EDGE Telefonu için  numaralı kart bilgileri alındı");

            return "1";
        } else if (deviceName.contains("3300ee33d8728319")) {
            logger.info("GALAXY J7 PRIME Telefonu için  numaralı kart bilgileri alındı");

            return "3";
        } else if (deviceName.contains("FA6A70302642")) {
            logger.info("GOOGLE PIXEL Telefonu için  numaralı kart bilgileri alındı");

            return "2";
        } else {
            logger.info("seçilmemiş telefon");
            return "1";
        }
    }

    @Step("Kazandıklarım internet ve diger karsılastırılması")
    public void karsilastirma() throws InterruptedException {
        String degerInternet = findElementByKey("HHinternet").getAttribute("name");
        String degerDiger = findElementByKey("HHdiger").getAttribute("name");
        clickByKey("kazandiklarim");
        waitBySecond(3);
        clickByKey("kazandiklarim2");
        waitBySecond(3);
        String degerInternet2 = findElementByKey("HHinternet").getAttribute("name");
        String degerDiger2 = findElementByKey("HHdiger").getAttribute("name");

        if (degerInternet == degerInternet2 && degerDiger == degerDiger2) {
            Assert.fail("Karşılaştırma başarısız");
        } else
            logger.info("Karşılaştırma başarılı");
    }

    @Step("AND Kazandıklarım internet ve diger karsılastırılması")
    public void karsilastirma2() throws InterruptedException {
        String degerInternet = findElementByKey("HHinternet").getAttribute("text");
        String degerDiger = findElementByKey("HHdiger").getAttribute("text");
        clickByKey("kazandiklarim");
        waitBySecond(3);
        clickByKey("kazandiklarim2");
        waitBySecond(3);
        String degerInternet2 = findElementByKey("HHinternet").getAttribute("text");
        String degerDiger2 = findElementByKey("HHdiger").getAttribute("text");

        if (degerInternet == degerInternet2 && degerDiger == degerDiger2) {
            Assert.fail("Karşılaştırma başarısız");
        } else
            logger.info("Karşılaştırma başarılı");
    }

    @Step("<key> elementi bulana kadar <StartX>,<StartY> Koordinatından <EndX>,<EndY> coordinatına <times> kere swipe et")
    public void pointToPointSwipeWithKoordinats(String key, int startX, int startY, int endX, int endY, int count) throws InterruptedException {
        Dimension d = appiumDriver.manage().window().getSize();
        MobileElement mobileElement;
        mobileElement = findElementByKeyWithoutAssert(key);

        for (int i = 0; i < count; i++) {
            if (mobileElement == null) {
                waitBySecond(3);
                TouchAction action = new TouchAction(appiumDriver);
                action.press(PointOption.point(startX, startY))
                        .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                        .moveTo(PointOption.point(endX, endY))
                        .release().perform();
                mobileElement = findElementByKeyWithoutAssert(key);

            } else {
                logger.info("element bulundu");
                break;
            }
        }
        for (int i = 0; i < count * 2; i++) {
            if (mobileElement == null) {
                waitBySecond(1);
                TouchAction action = new TouchAction(appiumDriver);
                action.press(PointOption.point(startX, endY))
                        .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                        .moveTo(PointOption.point(endX, startY))
                        .release().perform();
                mobileElement = findElementByKeyWithoutAssert(key);
            } else {
                logger.info("element bulundu");
                break;
            }
        }


    }

    public int currentTime() {

        Calendar now = Calendar.getInstance();
        int hour = now.get(Calendar.HOUR);
        logger.info(String.valueOf(hour));
        return hour;
    }

    @Step("son kullanma tarihi gir")
    public void enterSKT() throws InterruptedException {
        int ay = Integer.parseInt(HookImpl.kartBilgileri.getString(cardInformationNo() + "SktAy"));
        int yil = Integer.parseInt(HookImpl.kartBilgileri.getString(cardInformationNo() + "SktYil"));
        if (devicesPlatformAnd()) {
            int[] values = new int[3];
            int yukseklik, genislik, swipeStartPointX, swipeStartPointY, swipeEndPointY;
            String sinirDegerleriText = findElementByKey("sonKullanmaTarihi-Ay").getAttribute("bounds");
            values = makeStringToIntArray(sinirDegerleriText);
            yukseklik = values[3] - values[1];
            genislik = values[2] - values[0];
            swipeStartPointX = values[0] + (genislik / 2);
            swipeStartPointY = values[1] + (yukseklik / 2);
            swipeEndPointY = swipeStartPointY + ((genislik * 28) / 100);
            pointToPointSwipeWithCoordinats(swipeStartPointX, swipeStartPointY, swipeStartPointX, swipeEndPointY, 9);
            pointToPointSwipeWithCoordinats(swipeStartPointX, swipeEndPointY, swipeStartPointX, swipeStartPointY, ay - 2);
            sinirDegerleriText = findElementByKey("sonKullanmaTarihi-Yıl").getAttribute("bounds");
            values = makeStringToIntArray(sinirDegerleriText);
            yukseklik = values[3] - values[1];
            genislik = values[2] - values[0];
            swipeStartPointX = values[0] + (genislik / 2);
            swipeStartPointY = values[1] + (yukseklik / 2);
            swipeEndPointY = swipeStartPointY + ((genislik * 29) / 100);
            pointToPointSwipeWithCoordinats(swipeStartPointX, swipeEndPointY, swipeStartPointX, swipeStartPointY, yil - 2020);
        } else {
            sendKeysByKeyNotClear("sonKullanmaTarihi-Ay", String.valueOf(ay));
            sendKeysByKeyNotClear("sonKullanmaTarihi-Yıl", String.valueOf(yil));
        }
    }

    public int[] makeStringToIntArray(String text) {

        text = text.replaceAll("\\[", " ");
        text = text.replaceAll("]", " ");
        text = text.replaceAll(",", " ");
        text = text.replaceAll("  ", " ");
        int[] values = new int[4];
        int isaret = 1;
        int arrCount = 0;
        for (int i = 1; i < text.length(); i++) {
            if (text.substring(i, i + 1).equals(" ")) {
                values[arrCount] = Integer.parseInt(text.substring(isaret, i));
                isaret = i + 1;
                arrCount++;
            }
        }
        return values;
    }

    @Step("Mail adresslerini degistir")
    public void changeMail() throws InterruptedException {
        String mail = findElementByKey("tx_mailGuncelle").getAttribute("text").trim();

        logger.info(mail);
        if (mail == "mehtap.kaya@testinium.com") {
            clickByKey("tx_mailGuncelle");
            sendKeysByKey("tx_mailGuncelle", "buse.alp@testinium.com");
            hideAndroidKeyboard();
            clickByKey("btn_guncelle");

        } else
            logger.info("farklı mail");
    }

    @Step("<StartX>,<StartY> koordinatından <EndX>,<EndY> koordinatına <times> kere asagı swipe et")
    public void pointToPointDownSwipeWithCoordinats(int startX, int startY, int endX, int endY, int count) throws InterruptedException {
        Dimension d = appiumDriver.manage().window().getSize();

        for (int i = 0; i < count; i++) {
            waitBySecond(3);
            TouchAction action = new TouchAction(appiumDriver);
            action.press(PointOption.point(startX, endY))
                    .waitAction(WaitOptions.waitOptions(ofMillis(1000)))
                    .moveTo(PointOption.point(endX, startY))
                    .release().perform();
        }

    }

    @Step("Uygulamayı kapat ve tekrar ac")
    public void implementation1() throws MalformedURLException, InterruptedException {
        appiumDriver.quit();
        waitBySecond(5);
        if (StringUtils.isEmpty(System.getenv("key"))) {

            if (localAndroid) {
                logger.info("Local Browser");
                DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
                desiredCapabilities
                        .setCapability(MobileCapabilityType.PLATFORM, MobilePlatform.ANDROID);
                desiredCapabilities.setCapability(MobileCapabilityType.DEVICE_NAME, "android");
                desiredCapabilities.setCapability(MobileCapabilityType.UDID, "R58M40CLSFJ");
                desiredCapabilities
                        .setCapability(AndroidMobileCapabilityType.APP_PACKAGE,
                                "com.ttech.android.onlineislem");
                desiredCapabilities
                        .setCapability(AndroidMobileCapabilityType.APP_ACTIVITY,
                                "com.ttech.android.onlineislem.ui.splash.SplashActivity");
                // desiredCapabilities.setCapability(MobileCapabilityType.AUTOMATION_NAME, "uiautomator2");
                desiredCapabilities.setCapability(MobileCapabilityType.NO_RESET, true);
                desiredCapabilities.setCapability(MobileCapabilityType.FULL_RESET, false);
                desiredCapabilities.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, 300);
                desiredCapabilities.setCapability("unicodeKeyboard", false);
                desiredCapabilities.setCapability("resetKeyboard", false);
                URL url = new URL("http://127.0.0.1:4723/wd/hub");
                appiumDriver = new AndroidDriver(url, desiredCapabilities);
            } else {
                DesiredCapabilities desiredCapabilities = new DesiredCapabilities();
                // desiredCapabilities
                //       .setCapability(MobileCapabilityType.PLATFORM, MobilePlatform.IOS);
                desiredCapabilities.setCapability(MobileCapabilityType.AUTOMATION_NAME, "XCUITest");
                desiredCapabilities
                        .setCapability(MobileCapabilityType.UDID, "b6b570d596487b1c21780f8f1dce94f18cc257b2");
                desiredCapabilities
                        .setCapability(IOSMobileCapabilityType.BUNDLE_ID, "com.turkcell.CSI");
                desiredCapabilities
                        .setCapability(MobileCapabilityType.DEVICE_NAME, "testinium's iPhone");
                desiredCapabilities.setCapability(MobileCapabilityType.PLATFORM_VERSION, "11.3");
                desiredCapabilities.setCapability(MobileCapabilityType.NO_RESET, true);
                desiredCapabilities.setCapability(MobileCapabilityType.FULL_RESET, false);
                desiredCapabilities.setCapability(MobileCapabilityType.NEW_COMMAND_TIMEOUT, 300);

                desiredCapabilities.setCapability("sendKeyStrategy", "setValue");

                URL url = new URL("http://127.0.0.1:4723/wd/hub");
                appiumDriver = new IOSDriver<>(url, desiredCapabilities);
            }
        } else {
            String hubURL = "http://hub.testinium.io/wd/hub";
            DesiredCapabilities capabilities = new DesiredCapabilities();
            System.out.println("key:" + System.getenv("key"));
            System.out.println("platform" + System.getenv("platform"));
            System.out.println("version" + System.getenv("version"));
            if (System.getenv("platform").equals("ANDROID")) {
                localAndroid = true;
                capabilities.setCapability("key", System.getenv("key"));
                capabilities
                        .setCapability(AndroidMobileCapabilityType.APP_PACKAGE,
                                "com.ttech.android.onlineislem");
                capabilities
                        .setCapability(AndroidMobileCapabilityType.APP_ACTIVITY,
                                "com.ttech.android.onlineislem.ui.splash.SplashActivity");
                capabilities.setCapability(MobileCapabilityType.AUTOMATION_NAME, "uiautomator2"); //changed
                capabilities.setCapability(MobileCapabilityType.NO_RESET, true);
                capabilities.setCapability(MobileCapabilityType.FULL_RESET, false);
                capabilities.setCapability("unicodeKeyboard", false);
                capabilities.setCapability("resetKeyboard", false);
                appiumDriver = new AndroidDriver(new URL(hubURL), capabilities);
            } else {
                localAndroid = false;

                // sonradan eklenen degişiklikler -------------------
                capabilities.setCapability(MobileCapabilityType.NO_RESET, true);
                capabilities.setCapability(MobileCapabilityType.FULL_RESET, false);
                //---------------------------------------
                //capabilities.setCapability(CapabilityType.PLATFORM, Platform.MAC);
                capabilities.setCapability("usePrebuiltWDA", true); //changed
                // capabilities.setCapability("maxTypeFrequency", 5);
                capabilities.setCapability("key", System.getenv("key"));
                capabilities.setCapability("waitForAppScript", "$.delay(1000);");
                capabilities.setCapability("bundleId", "com.turkcell.CSI");
                capabilities.setCapability("usePrebuiltWDA", true);
                capabilities.setCapability("useNewWDA", true);
                appiumDriver = new IOSDriver(new URL(hubURL), capabilities);
            }
        }

        waitBySecond(5);
        //iki senaryo çeşidi aynı step te yazıldı ayrım senaryo ismine göre yapılıyor. ve step hibrit yazıldı
        if (senarioName.contains("Beni Unut")) {
            Assert.assertTrue(
                    "5307385720 numarası ile giriş yapılı olması gerekiyordu. Lütfen ilk logini hangi numara ile yaptıgını kontrol edin",
                    doesElementExistByKey("anasayfaGirisYapButonu", 10));
        } else {
            Assert.assertTrue(
                    "5307385720 numarası ile giriş yapılı olması gerekiyordu. Lütfen ilk logini hangi numara ile yaptıgını kontrol edin",
                    !doesElementExistByKey("anasayfaGirisYapButonu", 10));
        }


    }

    @Step("<key> value null a esitle")
    public void nullEqual(String key) {

    }

    @Step("Sifresiz hızlı giris yap")
    public void hizliGiris() throws InterruptedException {
       if( findElementByKey("hataligirdiniz") != null ){
           sendKeysByKeyNotClear("tekKullanimlikSifreAlani","1345");
           hideAndroidKeyboard();
           clickByKey("sifresizDevamEtBtn");
           getPageSourceFindWord("yanlış");



       }
        else
            logger.info("3 kere hatalı şifre girilmiş");
    }
}

