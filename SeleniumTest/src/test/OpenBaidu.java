package test;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.Point;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;


public class OpenBaidu {

	public static void main(String args[]) throws InterruptedException {

		/*System.setProperty("webdriver.chrome.driver","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");//chromedriver�����ַ
        WebDriver driver =new ChromeDriver(); //�½�һ��WebDriver �Ķ���
        driver.get("http://www.baidu.com");//��ָ������վ
        // �������ͬ���ǳ���Ҫ������ȴ�������������
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
        for(int i=0;i<5;i++)
        {
        	driver.findElement(By.id("kw")).clear();
        	driver.findElement(By.id("kw")).sendKeys(new  String[] {"hello world"});//�ҵ�kwԪ�ص�id��Ȼ������hello
        	driver.findElement(By.id("su")).click(); //�����Ť
        	Thread.sleep(1000);
        	try {
                
                driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
                

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        
        
        
        //dr.quit()��dr.close()�������˳������,�򵥵�˵һ�����ߵ����𣺵�һ��close��
        //������˶��ҳ���ǹز��ɾ��ģ���ֻ�رյ�ǰ��һ��ҳ�档�ڶ���quit��
      	//���˳�������Webdriver���еĴ��ڣ��˵ķǳ��ɾ��������Ƽ�ʹ��quit��Ϊһ��case�˳��ķ�����

        Thread.sleep(1000);
        driver.navigate().to("https://cn.bing.com/");
        // ˢ�������
        driver.navigate().refresh();
        // ���������
        driver.navigate().back();
        // �����ǰ��
        //driver.navigate().forward();
        Thread.sleep(5000);
        driver.close();*/
        
        
        System.setProperty("webdriver.chrome.driver","C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe");//chromedriver�����ַ
        WebDriver driver =new ChromeDriver(); //�½�һ��WebDriver �Ķ���
        //driver.manage().window().maximize();
        driver.manage().window().setPosition(new Point(100, 50));
        driver.manage().deleteAllCookies();
        // �������ͬ���ǳ���Ҫ������ȴ�������������
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
 
        driver.get("https://pan.baidu.com/");
 
        Thread.sleep(1000);
 
        WebElement qqLoginLink = driver
                .findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__footerULoginBtn\"]"));
        qqLoginLink.click();
        Thread.sleep(10);
 
        // ��ȡ��ǰҳ����
        String handle = driver.getWindowHandle();
        // ��ȡ����ҳ��ľ������ѭ���жϲ��ǵ�ǰ�ľ�� Ȼ���л����Ӵ���
        for (String handles : driver.getWindowHandles()) {
            if (handles.equals(handle))
                continue;
            driver.switchTo().window(handles);
        }
 
        // ���Թ����У������ʾ�Ҳ���Ԫ�أ���֪���Ƿ��л��ɹ��ˣ����԰ѵ�ǰhandler��source��ӡ��������
        System.out.println(driver.getPageSource());
 
        //driver.findElement(By.xpath("//*[@id='switcher_plogin']")).click();
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__userName\"]")).sendKeys("317409898");
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__password\"]")).sendKeys("xxxxxxxxx");
        Thread.sleep(500);
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__verifyCode\"]")).sendKeys("xxxx");
        driver.findElement(By.xpath("//*[@id=\"TANGRAM__PSP_4__submit\"]")).click();
         
        //�����ҵ��˺�û���ֻ������¼����и���ʾ�����ֱ�ӹرգ����ܱ��ж�Ϊ��û��ɵ�¼��û�лỰ�������Ե�Ƭ��
        Thread.sleep(2000);
         
        //�رյ������Ӵ���
        //driver.close();
         
        driver.navigate(); //���кܶ෽����������ˣ�ˢ�µ�
        Thread.sleep(2000);
        driver.navigate().to("https://cn.bing.com/");
        driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS); 
        Thread.sleep(2000);
        driver.navigate().back();
        Thread.sleep(2000);
        driver.close();
    }
 

}
