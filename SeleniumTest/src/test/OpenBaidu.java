package test;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;


public class OpenBaidu {

	public static void main(String args[]) throws InterruptedException {

		System.setProperty("webdriver.chrome.driver","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");//chromedriver�����ַ
        WebDriver driver =new ChromeDriver(); //�½�һ��WebDriver �Ķ��󣬵���new ����FirefoxDriver������
        driver.get("http://www.baidu.com");//��ָ������վ
        
        for(int i=0;i<10;i++)
        {
        	driver.findElement(By.id("kw")).clear();
        	driver.findElement(By.id("kw")).sendKeys(new  String[] {"hello"});//�ҵ�kwԪ�ص�id��Ȼ������hello
        	driver.findElement(By.id("su")).click(); //�����Ť
        	Thread.sleep(2);
        	try {
                
                driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
                

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        
        /**
         * dr.quit()��dr.close()�������˳������,�򵥵�˵һ�����ߵ����𣺵�һ��close��
         * ������˶��ҳ���ǹز��ɾ��ģ���ֻ�رյ�ǰ��һ��ҳ�档�ڶ���quit��
         * ���˳�������Webdriver���еĴ��ڣ��˵ķǳ��ɾ��������Ƽ�ʹ��quit��Ϊһ��case�˳��ķ�����
         */
        Thread.sleep(20);
        //driver.close();//�˳������

	}

 

}
