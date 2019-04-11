package test;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class OpenBaidu {

	public static void main(String args[]) throws InterruptedException {

		System.setProperty("webdriver.chrome.driver","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");//chromedriver服务地址
        WebDriver driver =new ChromeDriver(); //新建一个WebDriver 的对象，但是new 的是FirefoxDriver的驱动
        driver.get("http://www.baidu.com");//打开指定的网站
        
        for(int i=0;i<10;i++)
        {
        	driver.findElement(By.id("kw")).clear();
        	driver.findElement(By.id("kw")).sendKeys(new  String[] {"hello"});//找到kw元素的id，然后输入hello
        	driver.findElement(By.id("su")).click(); //点击按扭
        	Thread.sleep(2);
        	try {
                
                driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
                

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        
        /**
         * dr.quit()和dr.close()都可以退出浏览器,简单的说一下两者的区别：第一个close，
         * 如果打开了多个页面是关不干净的，它只关闭当前的一个页面。第二个quit，
         * 是退出了所有Webdriver所有的窗口，退的非常干净，所以推荐使用quit最为一个case退出的方法。
         */
        Thread.sleep(20);
        //driver.close();//退出浏览器

	}

 

}
