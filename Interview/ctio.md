## ✅ **1. What is a Technical Project Manager and what is your role?**

*A Technical Project Manager is someone who bridges technology and delivery. In my role, I don’t just manage timelines and reports—I actively guide the technical teams, remove roadblocks, and ensure the solution is implemented the right way.*
My responsibilities include:
* Acting as a **technical troubleshooter**—if ETL jobs fail, data is incorrect, APIs don’t work, or infrastructure breaks, I step in to guide the solution.
* Helping developers with **best technical approaches**, design decisions, and code review when required.
* Coordinating with **management and stakeholders** to give clear status, risks, and suggest better, cost-effective approaches.
* Ensuring we have the right **environments** — DEV, SIT, UAT, E2E, and proper backup/recovery.
* Driving **Agile sprint planning**, iteration goals, resource mentoring, and delivery governance.
* Making sure the project is delivered with **zero surprises**, minimal risk, and full stakeholder alignment.

---

## ✅ **2. Can you list 5 biggest challenges you faced and resolution?** 

*Siebel CRM Migration – Slow Delta Load & Cutover Bottleneck*

*Challenge:*
During the Siebel CRM migration, we had multiple source teams (IBM for OCR, Amdocs, and TCS for CPOS).
The Big Bang loads were manageable, but the **Delta loads during cutover night became extremely slow**.
The issue was that the **transformed data movement from staging to Siebel server was taking almost the same time as the full load**, which risked the cutover timeline.
*Resolution:*
I proposed performing a **minus-operation** between previous transformed tables and the new transformed data.
This reduced the dataset to **only incremental changes**, which significantly lowered data volume passed through the DB Link.
As a result, the **data transfer became faster and EIM load performance improved**, helping us meet the cutover window.

*High Error Records Coming from Source Systems*

*Challenge:*
Every week, large volumes of erroneous or unclean data were received from source systems, which later caused fallouts during migration.
*Resolution:*
I implemented a **weekly error-reporting framework** where all data quality issues were shared with business and source owners ahead of time.
Fixing these issues at the source helped us **dramatically reduce fallouts** during actual migration.

*Parallelizing Zone-Wise Migration to Meet Cutover Deadline*

*Challenge:*
During cutover, the four zones (North, East, West, South) were running one after another.
This caused idle waiting periods and increased the overall migration duration.
*Resolution:*
I redesigned the process and created a **customized zone-wise execution sequence** so that **all four EIM migrations could run in parallel**.
This minimized idle time, optimized resource usage, and helped us **meet the cutover deadline successfully**.

*Business Validation Taking Too Long**

*Challenge:*
Business validation and sign-offs used to take long hours because the business teams depended on daily CSV-based reports for counts and metrics.
*Resolution:*
I identified the exact reports the business relied on, optimized the SQL queries, and automated the logic to **compare daily business reports with cutover-night source data**.
This helped generate validation results instantly and significantly **reduced the BA validation and sign-off time**.

*Exadata Migration – Handling Delta Loads Efficiently*

*Challenge:*
During the Exadata migration, the delta migration was complex because continuous changes happened on the source transactional tables.
*Resolution:*
I designed a simple and efficient mechanism using **tablespace transport and endian conversion** for the bulk migration.
For delta migration, we created **triggers on critical tables to log all changes**.
We then migrated only these logged changes, which ensured consistency and improved performance.

*Mediation Database – Partition Creation Issue*

*Challenge:*
DBAs reported that new month-wise partitions could not be added due to default tablespace limitations.
*Resolution:*
I suggested splitting the **default tablespace into a separate tablespace for the new month’s partitions.
This allowed smooth partition creation and ensured continuity of the billing/mediation cycles.

“These challenges taught me to think analytically, optimize processes, and collaborate across teams. In all cases, I focused on reducing load time, improving data quality, and ensuring predictable cutover execution.”

---



## ✅ **3. What is ODA and product catalogue?** 

---

## ✅ **4. What were the CRM Migration Entities you migrated ?**

---

## ✅ **5. What are Vodafone processes for migration , BA and RA Signoff?**

---

## ✅ **6. What do you like about Netcracker?** 

---

## ✅ **7. Why are you leaving?** 

---

## ✅ **8. Why do you want to join 6d?**

---

## ✅ **9. What Challenges do you foresee here and plans to mitigate?** 

---

## ✅ **10. Why do you love telecom?** 

---

## ✅ **11. What are your hobbies?** 

---

## ✅ **12. Who are major stakholders in VF and your friends?** 

---

## ✅ **13. What is Migration Key and critical path?**

---

## ✅ **14. How will you handle pressure situation from  VF?**

---

## ✅ **15. What all migrations you did till now along with your roles impact and critically and what roles can u do here?**

---

## ✅ **16. How do you resolve conficts ?**

---

## ✅ **17. Your ideas for bulk load?**

---

## ✅ **18. What did u learn in nc and values u can add here?**

---

## ✅ **19. How do you plan to migrate amdocs to 6d?**

---

## ✅ **20. How can u help 6d?**

---

## ✅ **21. How do you Identify risks before hand and mitigation?** 

---

## ✅ **22. Some practical understanding about tlo slo proces discount account customer and party?**

---

## ✅ **23. Some practical understanding about network elements in hlr vlr etc gsm how call connects?**

---

## ✅ **24. Prepaid upss tables structures?** 


---
