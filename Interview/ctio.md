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

*These challenges taught me to think analytically, optimize processes, and collaborate across teams. In all cases, I focused on reducing load time, improving data quality, and ensuring predictable cutover execution and focussing on critical path.*

**1. Siebel CRM Migration – Slow Delta Load & Cutover Bottleneck**

**Challenge:**

During the Siebel CRM migration, we had multiple source teams (IBM for OCRM, Amdocs, and TCS for CPOS).
The Big Bang loads were manageable, but the **Delta loads during cutover night became extremely slow**.
The issue was that the **transformed data movement from staging to Siebel server was taking almost the same time as the full load**, which risked the cutover timeline.

**Resolution:**

I proposed performing a **minus-operation** between previous transformed tables and the new transformed data.
This reduced the dataset to **only incremental changes**, which significantly lowered data volume passed through the DB Link.
As a result, the **data transfer became faster and EIM load performance improved**, helping us meet the cutover window.

**2. High Fallouts Coming from Source Systems**

**Challenge:**

Lots of source system irregulalites were causing fallouts during migration. like slos missing, inactive products, family plans functional issues

**Resolution:**

I implemented a **weekly error-reporting framework** where all data quality issues were shared with business and source owners ahead of time.
Fixing these issues at the source helped us **dramatically reduce fallouts** during actual migration.

**3. Parallelizing Zone-Wise Migration to Meet Cutover Deadline**

**Challenge:**

During cutover, the four zones (North, East, West, South) were running one after another.
This caused idle waiting periods and increased the overall migration duration.

**Resolution:**

I redesigned the process and created a **customized zone-wise execution sequence** so that **all four EIM migrations could run in parallel**.
This minimized idle time, optimized resource usage, and helped us **meet the cutover deadline successfully**.

**4. Business Validation Taking Too Long**

**Challenge:**

Business validation and sign-offs used to take long hours because the business teams depended on daily VSV-based reports for counts and metrics.

**Resolution:**

I identified the exact reports the business relied on, optimized the SQL queries, and automated the logic to **compare daily business reports with cutover-night source data**.
This helped generate validation results instantly and significantly **reduced the BA validation and sign-off time**.

**5. Exadata Migration – Handling Delta Loads Efficiently**

**Challenge:**

During the Exadata migration, the delta migration was complex because continuous changes happened on the source transactional tables.

**Resolution:**

I designed a simple and efficient mechanism using **tablespace transport and endian conversion** for the bulk migration.
For delta migration, we created **triggers on critical tables to log all changes**.
We then migrated only these logged changes, which ensured consistency and improved performance.

**6. Mediation Database – Partition Creation Issue**

**Challenge:**

DBAs reported that new month-wise partitions could not be added due to default tablespace limitations.

**Resolution:**

I suggested splitting the **default tablespace into a separate tablespace for the new month’s partitions.
This allowed smooth partition creation and ensured continuity of the billing/mediation cycles.**


---



## ✅ **3. What is ODA and product catalogue and what do you know about Amdocs billing ?** 

## **1️⃣ What is ODA (TM Forum Open Digital Architecture)?**

* **ODA is a modern blueprint for telecom IT systems** — cloud-native, API-driven, and modular.
* It breaks legacy monolithic BSS/OSS into **standard reusable components** (Customer, Product, Ordering, Billing, Service, Resource, Analytics).
* All components communicate via **TMF Open APIs** (e.g., TMF620 Product, TMF622 Order, TMF629 Billing, etc.).
* Purpose:
  ✔ Faster digital service rollout
  ✔ Replace old CRM/Billing systems gradually
  ✔ Vendor interoperability
  ✔ Move telcos to cloud & microservices

**In simple words:**

> ODA is the modern way to build telecom BSS/OSS using standard APIs and modular components.

---

## **2️⃣ What is a Product Catalogue?**

* A **central repository of all sellable products/offers/bundles** and their pricing rules.
* It defines:
  ✔ Plans, add-ons, discounts, bundles
  ✔ Charging rules, validity, eligibility
  ✔ Dependencies (e.g., Postpaid plan + Add-on pack)
* The catalogue drives **ordering, provisioning, rating, and billing**.

**In Amdocs/telecom context:**

> Product Catalogue is the single source of truth for everything the operator can sell and how it is priced.

---

## **3️⃣ What is Amdocs Billing?**

Amdocs Billing is a **convergent revenue management system** that handles:

### **A) Customer/Account Model**

* Party → Account → Subscriber → Subscription
* Unified across CRM, billing and ordering.

### **B) Charging / Rating**

**Two flows:**

1. **CDR → Mediation → Batch Rating → Bill Run** (traditional postpaid)
2. **Real-Time Charging (OCS)** (prepaid, digital, 5G, API events)

### **C) Billing & Invoicing**

* Generates invoices, taxes, adjustments
* Manages Accounts Receivable
* Supports convergent billing (multiple services on one bill)

### **D) Key Components**

* Product Catalogue
* Mediation
* Rating Engine
* Real-Time Charging (OCS)
* Billing & AR

**In short:**

> Amdocs Billing handles customer hierarchy, usage processing, rating (batch/real-time), invoicing, and AR.

---

## **4️⃣ Migration Challenges (Amdocs → New System / ODA-based Stack)**

### **1. Data Model Misalignment**

* Amdocs uses large, relational, flat schemas.
* ODA uses API-driven JSON models (Party, Account, Product, Order).
* Requires **canonical mapping and transformation**.

### **2. Complex Customer Hierarchy**

* Party → Account → Subscriber → Subscription relationships
* Maintaining referential integrity across systems is challenging.

### **3. Product Catalogue Mis-match**

* Legacy plans may not fit modern ODA product structures.
* Requires **catalog harmonization** before migration.

### **4. Usage / CDR Migration**

* Reprocessing CDRs is risky.
* Need to ensure mediation normalization is consistent.

### **5. Real-time vs Batch Charging Differences**

* Prepaid balances, quotas, allowances must be synced precisely.
* Difficult if moving from batch to OCS-based real-time charging.

### **6. API-Based Loading Requirement**

* ODA microservices do **not** allow direct DB inserts.
* Data must be loaded via **TMF APIs**, not database scripts.
* Requires an ETL/migration engine that generates payloads.

### **7. Data Quality Issues**

* Amdocs often has years of legacy customer/product inconsistencies.
* Requires profiling, cleanup, dedupe, and validation frameworks.

### **8. Cutover & Parallel Run**

* Need to run both systems for a short period to validate invoices, rating, usage, etc.
* Ensuring **zero customer impact** is challenging.

---

# ⭐ **CRISP INTERVIEW VERSION (30-Second Summary)**

> “ODA is TM Forum’s modern, cloud-native blueprint that breaks telecom systems into modular, API-based components. The Product Catalogue defines all sellable plans and pricing. Amdocs Billing manages customer hierarchy, charging, rating, mediation, invoicing, and AR.
>
> In migrations, the biggest challenges come from mismatched data models, legacy catalog structures, and the need to transform Amdocs relational data into ODA-compliant JSON that can only be loaded via TMF APIs. Maintaining customer-account-subscription integrity, handling real-time vs batch charging differences, cleansing old data, and ensuring a clean cutover with parallel run are the major risks.”


Got it — here is a clear, **postpaid-only explanation** of **Real-Time Charging for postpaid customers**.
This is different from prepaid and is often misunderstood, so explaining it correctly impresses interviewers.

---

# 📘 **Real-Time Charging for Postpaid Customers**

### **1️⃣ Postpaid normally uses batch billing**

Traditional postpaid billing is:

```
CDR → Mediation → Rating (night batch) → Bill Run → Invoice
```

But modern postpaid systems **also use real-time charging features**, mainly for:

✔ Credit control
✔ Bill-shock prevention
✔ High-value services
✔ International roaming
✔ Fair-usage enforcement (postpaid data)

---

# 🚀 **2️⃣ What does Real-Time Charging mean in Postpaid?**

Real-Time Charging in postpaid is **not** deducting balance like prepaid.
Instead, it means:

### **✔ Real-time usage monitoring**

OCS receives data/voice/SMS events *as they happen*.

### **✔ Apply limits/controls immediately**

* Data cap reached? → throttle or charge extra
* Roaming activated? → apply real-time rules
* International calls? → check credit limit
* High premium-rate numbers? → block or alert

### **✔ Enforce credit limits**

If customer is nearing their **credit threshold**, OCS can:

* Send alerts
* Temporarily restrict certain services
* Suspend outgoing calls
* Allow certain free channels (incoming, emergency)

### **✔ Prevent bill shocks**

If usage suddenly spikes (e.g., roaming internet), OCS stops or slows usage *before* it becomes a massive bill.

---

# 🔍 **3️⃣ Why do postpaid operators use OCS?**

Because modern telco networks require **real-time decisioning** for:

### 📡 Postpaid Data Control (FUP)

Example:

* Plan: 50GB
* After 50GB → throttle to 64kbps
* Using OCS + PCRF/PCF to enforce changes in real-time

### 🌍 International Roaming Control

Events are checked in real time:

* If roaming pack is active → allow
* If not → block or redirect
* If usage is too high → suspend
* Alerts sent immediately

### 🧾 Bill-Shock Control

If a postpaid user crosses:

* 80% of data
* 100% data
* credit limit

OCS triggers action instantly.

---

# 🧠 **4️⃣ Postpaid Real-Time Charging Flow (Simple)**

```
Network Event (Data/Voice/SMS)
           ↓
    OCS (Real-Time Charging)
           ↓
Check postpaid conditions:
 - roaming rules?
 - FUP/data caps?
 - premium usage?
 - credit limit?
           ↓
Return action:
  ALLOW / THROTTLE / BLOCK / ALERT
           ↓
Usage is recorded (UDRs/CDRs)
           ↓
Batch billing rates the usage at bill cycle
```

---

# 🆚 **Batch Billing vs Real-Time Charging (Postpaid)**

| Feature                     | Batch Billing                | Real-Time Control (OCS) in Postpaid |
| --------------------------- | ---------------------------- | ----------------------------------- |
| When rating happens         | End of day or cycle          | Instant decisioning                 |
| Blocks usage                | No                           | Yes (only if rules violated)        |
| Data cap control            | After bill                   | Real-time throttle                  |
| Credit limit                | Checked only at billing time | Monitored live                      |
| Roaming                     | Rated after usage            | Controlled real-time                |
| Postpaid revenue protection | Weak                         | Strong                              |

---

# ⭐ **Short 20-second interview answer**

> “Postpaid mainly uses batch billing, but modern operators also use real-time charging through an OCS. In postpaid, real-time charging doesn’t deduct balance — instead it monitors usage instantly for things like data caps, bill-shock, roaming, premium services and credit limits. The OCS authorizes or restricts usage in real time, while the actual monetary rating happens later during the bill run. This gives postpaid customers protection, accuracy, and controlled usage.”


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

## ✅ **25. IOT?** 


---
