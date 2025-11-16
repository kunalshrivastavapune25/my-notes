## ✅ **1. What is a Technical Project Manager and what is your role?**

*A Technical Project Manager is someone who bridges technology and delivery. In my role, I don’t just manage timelines and reports—I actively guide the technical teams, remove roadblocks, and ensure the solution is implemented the right way.*

My responsibilities include:

* Acting as a **technical troubleshooter**—if ETL jobs fail, data is incorrect, APIs don’t work, or infrastructure breaks, I step in to guide the solution.
* Helping developers with **best technical approaches**, design decisions, and code review when required.
* Coordinating with **management and stakeholders** to give clear status, risks, and suggest better, cost-effective approaches.
* Ensuring we have the right **environments** — DEV, SIT, UAT, E2E, and proper backup/recovery.
* Driving **Agile sprint planning**, iteration goals, resource mentoring, and delivery governance.
* Making sure the project is delivered with **zero surprises**, minimal risk, and full stakeholder alignment.
* it's iteration based migration where functionalities keep added in nc and post uat, we ask that much data from source and migrate , we give product catalogue to them before each migration iteration 
---

## ✅ **2. Can you list 5 biggest challenges you faced and resolution?** 

*These challenges taught me to think analytically, optimize processes, and collaborate across teams. In all cases, I focused on reducing load time, improving data quality, and ensuring predictable cutover execution and focussing on critical path. We get these knowledge from dry and mock runs *

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

“In the CRM migration project, I migrated the core customer-centric entities required for a full Order-to-Cash flow.

The major entities included:
• Party / Customer Profile
• Accounts (Billing, Contact, Hierarchies)
• Subscribers / MSISDN / Services
• Subscriptions & Plans
• Products / Offers / Discounts
• Contact Details & Preferences
• Addresses & Identifications (KYC)
• Payment Methods / Deposit / Credit Limit
• Usage history / Transactions (selective)
• Trouble Tickets / Interaction History (as applicable)

Along with that, I handled the related reference data, lookup tables, relationship mapping, and ensured data integrity across Party → Account → Subscription → Product.

I also worked on delta loads, validations, EIM loads, and BA signoff processes to ensure clean cutover.”

---

## ✅ **5. What are Vodafone processes for migration , BA and RA Signoff?**

“Vodafone follows a very structured and disciplined migration process involving functional alignment, data validation, business signoff, and revenue assurance checks.

The major steps I worked on were:

1️⃣ Functional Mapping, Gap Analysis & Environment Setup

• First, we perform functionality mapping between the legacy system and the target system.
• Conduct gap analysis to understand what needs customization.
• Configure the new system, load reference data, and complete SIT + UAT before migration starts.

2️⃣ Big Bang Load + Delta Strategy

• We follow Vodafone’s Big Bang → Delta approach:

Big Bang Load: migrate all historical + current entities.

Delta Load: only incremental changes on cutover night.
• Delta execution is tightly coordinated with the application teams so that cutover is smooth.

3️⃣ Parallel Run Data Cleanup (Very Important)

• During parallel phases, every week we send erroneous or inconsistent data back to business teams.
• The goal is to get the source data cleaned before cutover, so that we minimize fallouts.
• This proactive cleanup step is a standard Vodafone practice and reduces load failures drastically.

4️⃣ BA Signoff (Business Assurance / Business Analyst Signoff)

• BA signoff means:

The data migrated from source matches with the BAU business reports used by the business.

Counts, totals, customer/account/product mappings—all validated.
• Before shutting down the old source system, business must confirm:
“Yes, the migrated data is correct and operationally usable.”
• We used optimized SQL scripts, validation reports, and comparison logic to ensure quick signoff.

5️⃣ RA Signoff (Revenue Assurance Signoff)

• RA verifies that all revenue-impacting data is migrated correctly, including:

usage buckets

billing accounts

deposits, balances

discounts, charges
• Their objective is to ensure zero revenue leakage.
• RA approves the migration only if all controls, thresholds, and cross-system values match.

6️⃣ Final Cutover

• After BA + RA signoff, we freeze the source system.
• Run final delta load in sync with downstream systems.
• Activate the new system and validate end-to-end flows.

This governance-based approach ensures high accuracy, clean data, and zero revenue leakage during migration for Vodafone.”

⭐ One-Line Summary (if interviewer asks quickly)

“Vodafone’s migration process consists of function mapping, Big Bang + Delta loads, parallel data cleanup, BA signoff for business data correctness, RA signoff for revenue accuracy, and controlled cutover with full application sync.”

---

## ✅ **6. What do you like about Netcracker?** 

“Netcracker is an excellent place to work because of its strong telecom domain, structured delivery model, and the opportunity to work on large transformation programs.

I really appreciated:
• The exposure to large tier-1 operator environments
• Working with BSS/OSS domains end-to-end
• Strong technical teams in billing, CRM and mediation
• Learning discipline — documentation, CAB, release process

It has given me strong fundamentals in migration, data engineering, billing systems, and customer management systems. I’m genuinely grateful for the learning and domain depth Netcracker provides.”

---

## ✅ **7. Why are you leaving?** 

“I’m looking for a role that offers more ownership and end-to-end responsibility.

Netcracker has been great for domain experience, but the environment is highly product-centric and sometimes limits broader architectural exposure.

I want to work in a place where I can contribute in solution design, cloud modernization, data engineering, CI/CD, and cross-functional delivery, not just implementation.

So it’s a career progression decision — I want to work on more modern stacks and take larger responsibilities.”

---

## ✅ **8. Why do you want to join 6d?**

“6D is one of the fastest-growing digital BSS & telecom solution companies, and the work is much more aligned with the direction I want to grow.

What attracts me is:
• Modern cloud-native architecture
• Exposure to TMF ODA-based modular systems
• API-driven CRM/Charging/Billing
• Opportunity to work across data engineering + DevOps + migration

I want to join a company where I can contribute to end-to-end solution architecture, migrations, cloud integration, and data pipelines — and 6D provides exactly that environment.

Also, 6D’s culture is fast-paced, innovative, and allows people to take ownership rather than work in rigid, product-bound environments. That’s the next step I want in my career.”

---

## ✅ **9. What Challenges do you foresee here and plans to mitigate?** 

prabhat, himanshu, nirupamay, aditi, ajit, sujit, 
---

## ✅ **10. Why do you love telecom?** 

“Telecom excites me because it is a perfect blend of high-volume data, real-time systems, complex integrations, and evolving architecture standards like ODA and 5G.

No other industry handles such massive scale—millions of events per second, strict SLAs, critical charging, and multi-system orchestration.

Working in telecom gives me the opportunity to solve problems related to data migration, real-time charging, provisioning, billing, analytics, cloud adoption, and automation.

The complexity and the continuous innovation is why I love this domain.”

⭐ Super Short Answer (for rapid-fire)

“Telecom combines scale, complexity, and real-time technology. It keeps evolving, and solving problems at this scale is what I enjoy the most.”

---

## ✅ **11. What are your hobbies?** 

algotrading

---

## ✅ **12. Who are major stakholders in VF and your friends?** 

prabhat, himanshu, nirupamay, aditi, ajit, sujit,

---

## ✅ **13. What is Migration Key and critical path?**

Here are **clean, interview-ready explanations** for both **Migration Key** and **Critical Path** — exactly how they are asked in telecom/BSS/CRM migration interviews.

---

# ✅ **1. What is a Migration Key?**

### **Simple Definition**

A **Migration Key** is a **unique identifier** used to map a customer/account/subscription in the **source system** to its corresponding record in the **target system** during migration.

### **Why it is needed**

* Every system has different primary keys.
* During migration, you need a **consistent way** to match:

  * Customer → Customer
  * Account → Account
  * Subscription → Subscription
  * Product → Product

### **Typical Migration Keys used in Telecom**

| Entity         | Common Migration Key                    |
| -------------- | --------------------------------------- |
| Party/Customer | Customer Number / Party ID / KYC ID     |
| Account        | Account Number / Billing Account Number |
| Subscriber     | MSISDN / SIM / IMSI                     |
| Subscription   | Service ID / Plan ID                    |
| Products       | Product Code / Offer Code               |

### **Purpose**

* Identifies the record uniquely
* Ensures referential integrity
* Helps establish **cross-entity relationships** in the target system
* Used heavily in **delta loads** to know what changed

### **Interview-ready one-line answer**

> “Migration Key is the unique identifier that helps map source entities to target entities during migration. It ensures consistent linking of Customer → Account → Subscription → Product across systems.”

---

# ✅ **2. What is a Critical Path in Migration?**

### **Simple Definition**

**Critical Path** is the sequence of activities in a migration that **must** be completed on time for the entire migration to succeed.
If any task on the critical path gets delayed → the migration gets delayed.

### **In telecom migration terms**

During cutover, several tasks run in parallel:

* Source system freeze
* Big Bang load
* Delta load
* Customer/account load
* Subscription load
* Product load
* Rating/charging sync
* RA & BA validation
* Go/no-go decision
* Activation of new system

Out of these, a few tasks are **time-bound and dependent**, like:

* Big Bang load completion
* Delta load sync
* Referential validation
* RA/BA signoff
* Final data reconciliation
* Integration smoke tests

These form the **critical path**.

### **Why is it important?**

Because migration cutover windows are usually only **6–12 hours**, and any delay creates:

* Customer impact
* Billing failures
* Revenue leakage
* Rollback risk

### **Interview-ready one-line answer**

> “Critical Path is the set of migration activities that directly affect the cutover timeline. If any critical-path step gets delayed, the entire migration is delayed. It includes Big Bang load, delta loads, validations, RA/BA signoff, and integration readiness.”

---

# ⭐ **Combined Example (Perfect for Interview)**

> “In migrations, we define a Migration Key to uniquely map each entity between source and target systems.
>
> During cutover, we also identify the Critical Path — the list of mandatory, time-sensitive tasks such as Big Bang load, delta loads, RA/BA signoff, and final validations. Any delay in these tasks delays the overall migration.”


---

## ✅ **14. How will you handle pressure situation from  VF?**

Here is a **strong, confident, senior-level answer** tailored for Vodafone (VF), where pressure situations are very common during migration, cutover, billing cycles, RA/BA checks, and production issues.

This answer will make you look mature, composed, and experienced.

---

# ✅ **Interview-Ready Answer: How will you handle pressure situations from Vodafone?**

> “In Vodafone, pressure situations usually arise during cutover weekends, delta loads, billing cycles, and urgent data or RA-related escalations.
>
> I handle pressure through a structured and calm approach:
>
> **1️⃣ Stay composed and prioritize issues clearly**
> I break the problem into:
> • customer-impacting
> • revenue-impacting
> • dependency-based
> This helps me solve the most critical items first.
>
> **2️⃣ Follow Vodafone’s governance and communication model**
> I communicate proactively with PMO, BA, RA, application teams, and DBAs so everyone knows what is happening.
> Pressure increases only when people don’t have information. Clear updates reduce pressure immediately.
>
> **3️⃣ Use data and logs, not assumptions**
> Whether it’s a migration issue or a load failure, I rely on validation reports, logs, counters, and queries to identify the exact root cause quickly.
>
> **4️⃣ Coordinate parallel teams instead of working in isolation**
> Vodafone migrations are cross-functional.
> I quickly bring:
> • CRM team
> • Billing team
> • OCS/Provisioning
> • DBAs
> • Testing
> together on the same call to stabilize the situation.
>
> **5️⃣ Keep contingency and rollback plans ready**
> I always design migration steps with rollback and checkpoints in mind.
> This reduces stress because we know we can revert safely if needed.
>
> **6️⃣ Maintain professionalism even under pressure**
> Vodafone is a demanding customer, but they appreciate calm, ownership-driven engineers.
> I make sure to stay solution-focused, not emotional, and deliver with ownership.”
>
> **In short, I manage pressure through clarity, communication, structured problem solving, and calm leadership.**

---

# ⭐ **Short version (if time is less)**

> “I handle Vodafone pressure by staying calm, prioritizing correctly, communicating clearly with all stakeholders, and relying on data, logs, and process discipline.
> I never react emotionally—I stay solution-focused and keep contingency plans ready so we deliver without panic.”

---

# ⭐ **Impactful one-line closer**

> “Pressure doesn’t affect me because I prepare well, communicate clearly, and follow a structured problem-solving approach.”


---

## ✅ **15. What all migrations you did till now along with your roles impact and critically and what roles can u do here?**



---

## ✅ **16. How do you resolve conficts ?**

I resolve conflicts by staying objective, understanding both sides, and bringing the conversation back to facts and outcomes.

My approach is:
1️⃣ Listen to both parties without interrupting – people calm down when they feel heard.
2️⃣ Identify the root cause – usually it’s miscommunication, unclear ownership, or mismatched expectations.
3️⃣ Focus on facts, data, and scope – not emotions or assumptions.
4️⃣ Align everyone on the common goal – delivery, customer impact, or timeline.
5️⃣ Agree on next steps and owners so that the team moves forward.

I keep the discussion respectful, solution-driven, and ensure nobody feels blamed.
My aim is always to protect delivery and relationships.

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
