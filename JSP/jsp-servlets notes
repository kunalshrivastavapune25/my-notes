Step 1: Locate the TomCatfolder and place below idex.html file.

	folder:C:\Intel\TomCat10\webapps\Beer-v1
	<html>
		<body>
			
			<h1 align="center"> Beer Selection Page  </h1>
			
			<form method="POST" action = "SelectBeer.do">
				Select Beer Charactertics <p>
				Color:
				<select name = "color" size ="1">
					<option value="light"> light </option>
					<option value="amber"> amber </option>
					<option value="brown"> brown </option>
					<option value="dark"> dark </option>
				</select>
				<br><br>
				<center> <input type="SUBMIT"> </center>			
			</form>
		</body>
	</html>


Step 2: Stop and Start Tomcat from 
	folder:C:\Intel\TomCat10\bin

Step 3: Below Url should be accessable now 
http://localhost:8080/Beer-v1/form.html


Step 4: Place below BeerSelect.java file inside 
	C:\Intel\TomCat10\webapps\Beer-v1\WEB-INF\classes\BeerSelect.java

	import jakarta.servlet.*;
	import jakarta.servlet.http.*;
	import java.io.*;

	public class BeerSelect extends HttpServlet {

			public void doPost(HttpServletRequest request, HttpServletResponse response)
				throws ServletException, IOException {
				response.setContentType("text/html");
				PrintWriter out = response.getWriter();
				out.println("Beer Selection Advice <br>");
				String c = request.getParameter("color");
				out.println("<br> Got Beer Color " + c);

			}
	}


Step 5: compile the .java file so that .class files which is plateform independent gets created.

	javac -classpath C:\Intel\TomCat10\lib\servlet-api.jar C:\Intel\TomCat10\webapps\Beer-v1\WEB-INF\classes\BeerSelect.java


Step 6: Place below web.xml file.

	C:\Intel\TomCat10\webapps\Beer-v1\WEB-INF\web.xml

	<?xml version="1.0" encoding="UTF-8"?>

	<web-app xmlns="https://jakarta.ee/xml/ns/jakartaee"
	  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	  xsi:schemaLocation="https://jakarta.ee/xml/ns/jakartaee
						  https://jakarta.ee/xml/ns/jakartaee/web-app_5_0.xsd"
	  version="5.0"
	  metadata-complete="true">


	  <servlet>
		<servlet-name>Beer</servlet-name>
		<servlet-class>BeerSelect</servlet-class>
	  </servlet>
	  
	  
	  <servlet-mapping>
		<servlet-name>Beer</servlet-name>
		  <url-pattern>/SelectBeer.do</url-pattern>
	  </servlet-mapping>
	  

	</web-app>


Step 7: retest and enjoy.
http://localhost:8080/Beer-v1/form.html