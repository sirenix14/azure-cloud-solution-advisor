import streamlit as st

st.set_page_config(
    page_title="Azure Solution Advisor",
    page_icon="☁️",
    layout="wide"
)

# -----------------------------
# Azure Recommendation Logic
# -----------------------------

def recommend_services(app_type, users, data_size, security, availability, database):
    services = []

    # Application hosting
    if app_type in ["Web Application", "E-commerce", "REST API"]:
        services.append({
            "Requirement": "Application Hosting",
            "Azure Service": "Azure App Service",
            "Reason": "Managed platform for hosting scalable web applications and APIs."
        })

    # Database
    if database == "Relational Database":
        services.append({
            "Requirement": "Database",
            "Azure Service": "Azure SQL Database",
            "Reason": "Managed relational database with scalability and high availability."
        })
    else:
        services.append({
            "Requirement": "Database",
            "Azure Service": "Azure Cosmos DB",
            "Reason": "Globally distributed NoSQL database suitable for scalable applications."
        })

    # Storage
    if data_size in ["100 GB - 1 TB", "More than 1 TB"]:
        services.append({
            "Requirement": "File/Object Storage",
            "Azure Service": "Azure Blob Storage",
            "Reason": "Scalable object storage for large amounts of unstructured data."
        })

    # Security
    if security in ["High", "Critical"]:
        services.append({
            "Requirement": "Identity & Authentication",
            "Azure Service": "Microsoft Entra ID",
            "Reason": "Provides identity management and secure authentication."
        })

        services.append({
            "Requirement": "Secrets Management",
            "Azure Service": "Azure Key Vault",
            "Reason": "Securely stores keys, secrets, certificates and credentials."
        })

    # Monitoring
    services.append({
        "Requirement": "Monitoring",
        "Azure Service": "Azure Monitor",
        "Reason": "Provides application and infrastructure monitoring."
    })

    # Scaling
    if users in ["10,000 - 100,000", "More than 100,000"]:
        services.append({
            "Requirement": "Scalability",
            "Azure Service": "Azure Front Door",
            "Reason": "Provides global routing, acceleration and application availability."
        })

    # Availability
    if availability == "Critical":
        services.append({
            "Requirement": "High Availability",
            "Azure Service": "Azure Availability Zones",
            "Reason": "Protects applications from datacenter-level failures."
        })

    return services


def identify_risks(users, data_size, security, availability, budget):
    risks = []

    if security == "Low":
        risks.append({
            "Risk": "Weak Security Controls",
            "Severity": "High",
            "Recommendation": "Implement Microsoft Entra ID, Key Vault and network security controls."
        })

    if availability == "Critical":
        risks.append({
            "Risk": "Availability Requirement",
            "Severity": "High",
            "Recommendation": "Use Availability Zones and implement disaster recovery."
        })

    if users in ["10,000 - 100,000", "More than 100,000"]:
        risks.append({
            "Risk": "Scalability",
            "Severity": "Medium",
            "Recommendation": "Implement autoscaling and traffic distribution."
        })

    if data_size == "More than 1 TB":
        risks.append({
            "Risk": "Large Data Volume",
            "Severity": "Medium",
            "Recommendation": "Use Blob Storage and implement lifecycle management."
        })

    if budget == "Low":
        risks.append({
            "Risk": "Budget Constraint",
            "Severity": "Medium",
            "Recommendation": "Use managed services and monitor cloud consumption."
        })

    if not risks:
        risks.append({
            "Risk": "No Critical Risks Identified",
            "Severity": "Low",
            "Recommendation": "Continue monitoring application performance and cloud consumption."
        })

    return risks


# -----------------------------
# Header
# -----------------------------

st.title("☁️ Azure Cloud Solution Advisor")

st.write(
    """
    An interactive cloud solution advisory tool that converts customer
    business and technical requirements into Azure architecture,
    risk assessment and migration recommendations.
    """
)

st.divider()

# -----------------------------
# Sidebar
# -----------------------------

st.sidebar.header("Customer Requirements")

app_type = st.sidebar.selectbox(
    "Application Type",
    [
        "Web Application",
        "REST API",
        "E-commerce",
        "Data Analytics"
    ]
)

infrastructure = st.sidebar.selectbox(
    "Current Infrastructure",
    [
        "On-Premise",
        "AWS",
        "Local Server",
        "Existing Azure Environment"
    ]
)

users = st.sidebar.selectbox(
    "Expected Users",
    [
        "Less than 1,000",
        "1,000 - 10,000",
        "10,000 - 100,000",
        "More than 100,000"
    ]
)

data_size = st.sidebar.selectbox(
    "Data Size",
    [
        "Less than 100 GB",
        "100 GB - 1 TB",
        "More than 1 TB"
    ]
)

security = st.sidebar.selectbox(
    "Security Requirement",
    [
        "Low",
        "Medium",
        "High",
        "Critical"
    ]
)

availability = st.sidebar.selectbox(
    "Availability Requirement",
    [
        "Standard",
        "High",
        "Critical"
    ]
)

database = st.sidebar.selectbox(
    "Database Type",
    [
        "Relational Database",
        "NoSQL Database"
    ]
)

budget = st.sidebar.selectbox(
    "Budget Constraint",
    [
        "Low",
        "Medium",
        "High"
    ]
)

analyze = st.sidebar.button(
    "Analyze Solution",
    type="primary"
)

# -----------------------------
# Main Dashboard
# -----------------------------

if analyze:

    services = recommend_services(
        app_type,
        users,
        data_size,
        security,
        availability,
        database
    )

    risks = identify_risks(
        users,
        data_size,
        security,
        availability,
        budget
    )

    st.success("Solution analysis completed.")

    # -------------------------
    # Customer Summary
    # -------------------------

    st.header("1. Customer Requirement Summary")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Application", app_type)

    with col2:
        st.metric("Expected Users", users)

    with col3:
        st.metric("Security", security)

    with col4:
        st.metric("Availability", availability)

    st.write("**Current Infrastructure:**", infrastructure)
    st.write("**Data Size:**", data_size)
    st.write("**Database:**", database)
    st.write("**Budget Constraint:**", budget)

    # -------------------------
    # Architecture
    # -------------------------

    st.header("2. Recommended Azure Architecture")

    st.code(
        """
                         USERS
                           │
                           ▼
                  Azure Front Door
                           │
                           ▼
                   Azure App Service
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
       Azure SQL Database        Azure Blob Storage
              │
              │
              ▼
       Microsoft Entra ID
              │
              ▼
         Azure Key Vault

              │
              ▼
         Azure Monitor
        """,
        language="text"
    )

    # -------------------------
    # Service Recommendations
    # -------------------------

    st.header("3. Azure Service Recommendations")

    for service in services:

        st.subheader(service["Azure Service"])

        col1, col2 = st.columns([1, 2])

        with col1:
            st.write("**Requirement**")
            st.write(service["Requirement"])

        with col2:
            st.write("**Why?**")
            st.write(service["Reason"])

    # -------------------------
    # Risk Analysis
    # -------------------------

    st.header("4. Risk Assessment")

    for risk in risks:

        if risk["Severity"] == "High":
            st.error(
                f"🔴 HIGH RISK: {risk['Risk']}\n\n"
                f"Recommendation: {risk['Recommendation']}"
            )

        elif risk["Severity"] == "Medium":
            st.warning(
                f"🟠 MEDIUM RISK: {risk['Risk']}\n\n"
                f"Recommendation: {risk['Recommendation']}"
            )

        else:
            st.success(
                f"🟢 LOW RISK: {risk['Risk']}\n\n"
                f"Recommendation: {risk['Recommendation']}"
            )

    # -------------------------
    # Migration Strategy
    # -------------------------

    st.header("5. Cloud Migration Roadmap")

    migration_steps = [
        ("Phase 1", "Requirement Analysis",
         "Understand business requirements, technical constraints and stakeholder expectations."),

        ("Phase 2", "Solution Design",
         "Design Azure architecture based on scalability, security and availability requirements."),

        ("Phase 3", "Proof of Concept",
         "Validate the proposed architecture using a small-scale implementation."),

        ("Phase 4", "Migration",
         "Migrate application, databases and data to the selected Azure services."),

        ("Phase 5", "Testing",
         "Perform functional, security, performance and disaster recovery testing."),

        ("Phase 6", "Production Deployment",
         "Deploy the validated solution to the production environment."),

        ("Phase 7", "Optimization",
         "Monitor cloud consumption, performance and security and optimize the environment.")
    ]

    for phase, title, description in migration_steps:

        with st.expander(f"{phase} — {title}"):
            st.write(description)

    # -------------------------
    # Cloud Adoption Opportunities
    # -------------------------

    st.header("6. Cloud Adoption Opportunities")

    opportunities = [
        "Modernize on-premise applications using managed Azure services.",
        "Reduce infrastructure maintenance through Platform-as-a-Service.",
        "Implement centralized identity and authentication.",
        "Improve application monitoring using Azure Monitor.",
        "Improve scalability through autoscaling and distributed architecture.",
        "Improve security through centralized secrets management.",
        "Optimize cloud consumption through monitoring and resource management."
    ]

    for opportunity in opportunities:
        st.write("✅", opportunity)

    # -------------------------
    # Stakeholder Analysis
    # -------------------------

    st.header("7. Stakeholder Considerations")

    stakeholder_data = {
        "Stakeholder": [
            "Customer / Business Team",
            "Development Team",
            "Security Team",
            "Operations Team",
            "Project Manager"
        ],

        "Primary Concern": [
            "Cost, business value and delivery timeline",
            "Application performance and development effort",
            "Security and compliance",
            "Reliability and monitoring",
            "Scope, risks and project schedule"
        ]
    }

    st.table(stakeholder_data)

    # -------------------------
    # Final Recommendation
    # -------------------------

    st.header("8. Solution Summary")

    st.info(
        f"""
        Based on the provided requirements, the recommended approach is
        to migrate the {app_type.lower()} from {infrastructure.lower()}
        to a managed Azure architecture.

        The solution prioritizes {security.lower()} security,
        {availability.lower()} availability and scalability for
        approximately {users.lower()} users.

        The recommended architecture uses managed Azure services to
        reduce infrastructure management while improving monitoring,
        security and cloud adoption.
        """
    )

else:

    st.info(
        "👈 Enter customer requirements in the sidebar and click "
        "**Analyze Solution** to generate an Azure solution."
    )

    st.header("What this tool demonstrates")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📋 Requirements")
        st.write(
            "Converts customer business and technical requirements "
            "into technology decisions."
        )

    with col2:
        st.subheader("☁️ Cloud Solution")
        st.write(
            "Maps requirements to appropriate Microsoft Azure services."
        )

    with col3:
        st.subheader("⚠️ Risk Management")
        st.write(
            "Identifies technical risks and provides mitigation strategies."
        )
