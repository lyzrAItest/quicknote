Okay, here's the information formatted as a Markdown file, ready to be copied.

---

# AI-Powered Expense Tracking System: Agent & Tool Directory

This document outlines the sophisticated ensemble of AI agents and their supporting tools, meticulously designed to automate, optimize, and personalize your financial management experience, seamlessly integrating with the Google Wallet API.

## 1. Our Intelligent Agents

An advanced ecosystem of AI agents, each playing a crucial role in delivering a comprehensive expense tracking solution.

| Agent Name                | Core Role                                           | Key Responsibilities                                                                                             | Key Tools Used                          | Google Services                                             | Key LLM            |
| :------------------------ | :-------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- | :-------------------------------------- | :---------------------------------------------------------- | :----------------- |
| **Orchestrator Agent**    | Central Command & Intelligent Query Router          | - Intelligent Query Redirection<br/>- Direct Generic Question Answering                                          | N/A                                     | N/A (System-wide Orchestration)                             | N/A                |
| **Receipt Analyser Agent**| Precision Data Extractor & Secure Pass Generator    | - Advanced OCR & Data Extraction<br/>- User Confirmation & Validation<br/>- Google Wallet Pass Creation & Cloud Upload | Pass Creation Tool                      | Google Cloud API, Google Wallet API, Google Firestore DB    | gemini-2.5-pro     |
| **Financial Advisor Agent**| Proactive Financial Insight & Guidance Provider     | - Personalized Financial Advisory<br/>- Automated Daily Financial Tips                                          | DB_Tool                                 | Google Firestore DB, Google Wallet API                      | gemini-2.5-flash   |
| **Group Receipt Analyser Agent** | Collaborative Expense Distribution & Management | - Group Receipt Analysis<br/>- Dynamic Expense Splitting<br/>- Automated Pass Distribution to Members             | Group Split Tool, DB_Tool               | Google Firestore DB, Google Wallet API                      | N/A                |
| **Receipt Tracker Agent** | Expense Reconciliation & Pass Optimization Engine   | - Automated Item Matching & Fulfillment<br/>- Dynamic Google Wallet Pass Updates                                 | DB_Tool, Google Wallet Pass Tool        | Google Firestore DB, Google Wallet API                      | gemini-2.5-flash   |
| **Goal-Based Agent**      | Personalized Financial Goal Accelerator             | - Continuous Spending Monitoring<br/>- Proactive Progress Reminders (FCM)<br/>- Dynamic Goal Status Reporting     | DB_Tool, Notification Tool (FCM Based)  | Google Firestore DB, Notification Tool (FCM based)          | gemini-2.5-pro     |
| **Price Check Agent**     | Smart Shopper's Savings Maximizer                   | - Localized Price Comparison<br/>- Value Optimization Alerts (FCM)                                               | BrowserUse Agent (Tool), DB_Query       | Notification Tool (FCM based)                               | N/A                |
| **Analytics Agent**       | Comprehensive Financial Insights Provider           | - Dynamic Spending Analysis (Month/Week)<br/>- Data-Driven Reporting & Visualization                             | DB_Query, Text-to-SQL Agent             | Google Firestore DB                                         | N/A                |
| **Custom Dashboard Agent**| Personalized User Experience Architect              | - User Preference Integration<br/>- Dynamic Dashboard Tailoring (UI Support)                                     | DB_Query, Text-to-SQL Agent             | Google Firestore DB                                         | N/A                |

---

## 2. Core System Tools

The powerful utilities and integrations enabling seamless data flow, intelligent processing, and robust functionality across our AI agent ecosystem.

| Tool Name                       | Purpose                                                  | Core Functionality                                                                                                         | Key Integrations / Dependencies                  |
| :------------------------------ | :------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| **Pass Creation Tool**          | Generates Google Wallet Passes & Archives Receipts       | Establishes a direct, secure connection with the Google Wallet API to create new digital passes. Concurrently, uploads receipt data to Google Cloud Storage. | Google Wallet API, Google Cloud Storage          |
| **DB_Tool**                     | Universal Database Access & Manipulation                 | Securely queries, retrieves, and updates required financial and user-centric data from the Google Firestore Database.        | Google Firestore DB                              |
| **Group Split Tool**            | Automates Group Expense Allocation & Distribution        | Intelligently calculates and divides amounts from complex group receipts among specified users. Orchestrates automated dispatch of individual Google Wallet passes. | Google Wallet API                                |
| **Google Wallet Pass Tool**     | Dynamically Updates Existing Google Wallet Passes        | Directly interfaces with the Google Wallet API to modify or update details on previously created passes.                    | Google Wallet API                                |
| **Notification Tool (FCM Based)** | Delivers Real-time User Alerts & Reminders               | Utilizes Firebase Cloud Messaging (FCM) to send highly reliable and timely push notifications, personalized reminders, and critical alerts. | Firebase Cloud Messaging (FCM)                   |
| **BrowserUse Agent (Tool)**     | Enables Intelligent Web Data Retrieval                   | Operates as a specialized sub-agent that can autonomously browse the web, search for, and gather specific external data.  | External Web                                     |
| **DB_Query**                    | Natural Language to SQL Translator & Executor            | Transforms natural language requests for data into precise SQL queries. Executes these queries against the database to retrieve and deliver results. | Text-to-SQL Agent, Database (e.g., Firestore)    |
| **Text-to-SQL Agent**           | Semantic Understanding & Dynamic SQL Generation Engine   | Given the schema of all relevant database tables, dynamically generates accurate and optimized SQL queries from natural language descriptions or data requirements. | Database Schema                                  |
