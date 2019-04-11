package test;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class OpenBaidu {

	public static void main(String args[]) throws InterruptedException {

		/*System.setProperty("webdriver.chrome.driver","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");//chromedriver服务地址
        WebDriver driver =new ChromeDriver(); //新建一个WebDriver 的对象
        driver.get("http://www.baidu.com");//打开指定的网站
        // 与浏览器同步非常重要，必须等待浏览器加载完毕
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        for(int i=0;i<5;i++)
        {
        	driver.findElement(By.id("kw")).clear();
        	driver.findElement(By.id("kw")).sendKeys(new  String[] {"hello world"});//找到kw元素的id，然后输入hello
        	driver.findElement(By.id("su")).click(); //点击按扭
        	Thread.sleep(1000);
        	try {
                
                driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
                

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        
        
        //dr.quit()和dr.close()都可以退出浏览器,简单的说一下两者的区别：第一个close，
        //如果打开了多个页面是关不干净的，它只关闭当前的一个页面。第二个quit，
      	//是退出了所有Webdriver所有的窗口，退的非常干净，所以推荐使用quit最为一个case退出的方法。

        Thread.sleep(1000);
        driver.navigate().to("https://cn.bing.com/");
        // 刷新浏览器
        driver.navigate().refresh();
        // 浏览器后退
        driver.navigate().back();
        // 浏览器前进
        //driver.navigate().forward();
        Thread.sleep(5000);
        driver.close();*/
        
        
        System.setProperty("webdriver.chrome.driver","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");//chromedriver服务地址
        WebDriver driver =new ChromeDriver(); //新建一个WebDriver 的对象
        //driver.manage().window().maximize();
        driver.manage().window().setPosition(new Point(100, 50));
        driver.manage().deleteAllCookies();
        // 与浏览器同步非常重要，必须等待浏览器加载完毕
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
 
        driver.get("https://pan.baidu.com/");
 
        Thread.sleep(1000);
 
        WebElement qqLoginLink = driver
                .findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__footerULoginBtn\"]"));
        qqLoginLink.click();
        Thread.sleep(10);
 
        // 获取当前页面句柄
        String handle = driver.getWindowHandle();
        // 获取所有页面的句柄，并循环判断不是当前的句柄 然后切换到子窗体
        for (String handles : driver.getWindowHandles()) {
            if (handles.equals(handle))
                continue;
            driver.switchTo().window(handles);
        }
 
        // 调试过程中，如果提示找不到元素，不知道是否切换成功了，可以把当前handler的source打印出来看看
        System.out.println(driver.getPageSource());
 
        //driver.findElement(By.xpath("//*[@id='switcher_plogin']")).click();
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__userName\"]")).sendKeys("317409898");
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__password\"]")).sendKeys("xxxxxxxxx");
        Thread.sleep(500);
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__verifyCode\"]")).sendKeys("xxxx");
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__submit\"]")).click();
         
        //由于我的账号没绑定手机，点登录后会有个提示，如果直接关闭，可能被判断为还没完成登录，没有会话，所以稍等片刻
        Thread.sleep(2000);
         
        //关闭弹出的子窗体
        //driver.close();
         
        driver.navigate(); //下有很多方法，比如后退，刷新等
        Thread.sleep(2000);
        driver.navigate().to("https://cn.bing.com/");
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
        Thread.sleep(2000);
        driver.navigate().back();
        Thread.sleep(2000);
        driver.close();
    }
 

}
