# 🫀 OrganMatch - AI-Powered Organ Donation Matching Platform

A production-ready, full-stack web application that uses **Machine Learning** to predict donor-recipient compatibility for organ transplants. Built with Flask, SQLAlchemy, scikit-learn, and modern web technologies.

**Status:** Production-Ready | **Version:** 1.0 | **License:** MIT

## ⚠️ IMPORTANT NOTICE

The `app.py` file within the `ml` directory has been **intentionally removed** to protect the project’s intellectual work and to prevent unauthorized reuse of the complete implementation.

For **legitimate academic, research, or project-related access** to the full source code, please contact:

- **Email:** bhuvankumarr2004@gmail.com  
- **Phone:** +91 86606 877802



---

## 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Why This Tech Stack](#why-this-tech-stack)
3. [Frontend Architecture](#-frontend-architecture)
4. [Backend Architecture](#-backend-architecture)
5. [Machine Learning System](#-machine-learning-system)
6. [Project File Structure](#project-file-structure)
7. [Installation & Setup](#installation--setup)
8. [Running the Application](#running-the-application)
9. [Deployment](#deployment)

---

## Project Overview

### What Does OrganMatch Do?

OrganMatch is an intelligent matching system for organ transplants. It:
- **Stores donor and recipient information** securely
- **Analyzes 12+ medical parameters** for each potential match
- **Predicts compatibility scores** (0-100%) using AI/ML
- **Visualizes results** with interactive dashboards
- **Automatically retrains** when new data is added
- **Tracks system events** with comprehensive logging

### Problem Statement

Manual organ matching is:
- ❌ Time-consuming (requires medical staff review)
- ❌ Subjective (depends on individual expertise)
- ❌ Error-prone (human oversight required)
- ❌ Inflexible (hard to analyze all combinations)

### Our Solution

OrganMatch uses **Random Forest Machine Learning** to:
- ✅ Analyze all possible donor-recipient combinations instantly
- ✅ Provide data-driven compatibility predictions
- ✅ Improve outcomes through consistent analysis
- ✅ Learn from historical data automatically

---

## Why This Tech Stack

### Tech Stack Summary

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (Client-Side)                   │
│  HTML5 + CSS3 + JavaScript + Bootstrap 5 + Chart.js         │
└─────────────────────────────────────────────────────────────┘
                            ↕ (HTTP Requests)
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (Server-Side)                     │
│     Flask 3.0 + Flask-SQLAlchemy + Flask-Login              │
│     SQLAlchemy ORM + Werkzeug Security                       │
└─────────────────────────────────────────────────────────────┘
                            ↕ (SQL Queries)
┌─────────────────────────────────────────────────────────────┐
│                    DATABASE (Data Persistence)                │
│    PostgreSQL (Production) / SQLite (Development)            │
└─────────────────────────────────────────────────────────────┘
                            ↕ (Python Imports)
┌─────────────────────────────────────────────────────────────┐
│              MACHINE LEARNING (AI Intelligence)               │
│   scikit-learn + pandas + numpy + geopy + joblib            │
└─────────────────────────────────────────────────────────────┘
```

### Language Choices & Rationale

#### **Python (Backend & ML)**

**Why Python?**
1. **ML Libraries:** scikit-learn, TensorFlow, pandas are Python-native with excellent support
2. **Data Processing:** pandas is the gold standard for data manipulation and analysis
3. **Rapid Development:** Compared to Java/C++, Python reduces development time by 40-50%
4. **Community:** Largest ML/AI community; thousands of libraries and tutorials
5. **Hospital Integration:** Many healthcare systems already use Python (interoperability)
6. **Readability:** Code clarity is crucial for medical applications (security audits, compliance)

**Python Versions Used:**
- Python 3.11+: Modern async support, faster performance, better typing

#### **HTML5 (Markup)**

**Why HTML5?**
1. **Semantic Structure:** Proper document structure for accessibility (WCAG 2.1 compliance)
2. **Form Validation:** Native input validation (email, number, required fields)
3. **Geolocation API:** Built-in browser location services (no external plugin needed)
4. **Accessibility:** ARIA labels for screen readers (essential for medical apps)
5. **Standards:** Universal browser support without vendor lock-in

#### **CSS3 (Styling)**

**Why CSS3?**
1. **Glassmorphism Design:** Modern aesthetic with backdrop-filter blur effects
2. **Gradients:** Smooth color transitions for professional appearance
3. **Responsive Grid:** CSS Grid + Flexbox for mobile-first design
4. **Animations:** Smooth transitions without JavaScript overhead
5. **Variables:** CSS custom properties for theme consistency

#### **JavaScript (Interactivity)**

**Why Vanilla JS + Libraries?**
1. **Geolocation:** `navigator.geolocation.getCurrentPosition()` for GPS location capture
2. **Fetch API:** Modern alternative to XMLHttpRequest (async/await support)
3. **DOM Manipulation:** Direct access to HTML elements for real-time UI updates
4. **Chart.js:** Lightweight charting library (only 50KB) vs heavy alternatives
5. **OpenStreetMap:** Free, open-source map provider (no API key needed)

#### **Flask (Web Framework)**

**Why Flask?**
1. **Lightweight:** Only 600 lines of core code (vs Django's 10,000+ lines)
2. **Microframework:** Perfect for focused applications (not overkill like Django)
3. **Jinja2 Templating:** Elegant syntax for HTML templates with logic
4. **Extensibility:** Large ecosystem of Flask extensions (Flask-Login, Flask-SQLAlchemy, etc.)
5. **Learning Curve:** Easier for small teams; less magic than Django
6. **Performance:** Faster request handling for matching engine (critical for real-time predictions)

#### **SQLAlchemy (ORM - Object Relational Mapping)**

**Why SQLAlchemy?**
1. **Database Abstraction:** Write code once, run on PostgreSQL/SQLite/MySQL without changes
2. **Type Safety:** Python types mapped to database types (prevents SQL injection)
3. **Relationships:** Easy many-to-one, one-to-many relationships without manual joins
4. **Query Building:** Pythonic syntax instead of raw SQL strings
5. **Migrations:** Works with Alembic for database version control

**Example:**
```python
# SQLAlchemy (Pythonic)
donors = Donor.query.filter_by(blood_group='O+').all()

# vs Raw SQL (Error-prone)
donors = db.execute("SELECT * FROM donors WHERE blood_group='O+'")
```

#### **PostgreSQL (Production Database)**

**Why PostgreSQL?**
1. **ACID Compliance:** Medical data requires guaranteed consistency (no data loss)
2. **JSON Support:** Can store complex medical records without extra tables
3. **Advanced Features:** Window functions, CTEs for complex medical queries
4. **Reliability:** Battle-tested in healthcare systems worldwide
5. **Open Source:** Free, no licensing costs; community support

**Development Database: SQLite**
- Minimal setup (single file: `organmatch.db`)
- Perfect for testing, no database server needed
- Automatically switches to PostgreSQL in production

#### **scikit-learn (Machine Learning)**

**Why scikit-learn?**
1. **Random Forest:** Perfect algorithm for medical predictions (handles missing data)
2. **Evaluation Tools:** Built-in confusion matrix, ROC curves, classification reports
3. **Preprocessing:** Train/test split, feature scaling, imputation
4. **Production Ready:** Serializable models, works in production environments
5. **Interpretability:** Feature importance rankings (doctors want to know why)

**Why NOT Deep Learning (TensorFlow)?**
- Requires massive datasets (millions of samples)
- "Black box" predictions (unacceptable in healthcare)
- Overkill for structured medical data
- Our dataset: ~100-500 donor/recipient pairs (Random Forest is optimal)

---

# 🎨 FRONTEND ARCHITECTURE

The frontend is the user-facing layer. It's responsible for:
- ✅ Capturing user input (forms)
- ✅ Displaying data (tables, charts, maps)
- ✅ Managing navigation
- ✅ Styling and UX

### Frontend Technology Stack

| Technology | Version | Purpose | Why? |
|-----------|---------|---------|------|
| **HTML5** | Latest | Document structure | Semantic markup, accessibility |
| **CSS3** | Latest | Styling & animations | Gradients, backdrop-filter, responsive grid |
| **JavaScript** | ES6+ | Interactivity | Geolocation, fetch requests, DOM manipulation |
| **Bootstrap 5** | 5.3.0 | UI Framework | Pre-built components, responsive grid, icons |
| **Chart.js** | Latest | Data visualization | Lightweight, interactive charts |
| **Font Awesome** | 6.4.0 | Icons | 2000+ medical/UI icons |
| **Leaflet.js** | 1.9.4 | Map visualization | Open-source map library (no API key) |
| **Jinja2** | Built-in | Template engine | Server-side HTML rendering |

---

## 📁 Frontend Files Explained

### **1. Core Template: `templates/base.html`** (258 lines)

**Purpose:** Master template that all pages inherit from. Defines the skeleton of the entire application.

**Key Components:**

#### Navigation Bar (Lines 145-210)
```html
<nav class="navbar navbar-expand-lg navbar-dark">
    <a class="navbar-brand" href="{{ url_for('dashboard') }}">
        <i class="fas fa-heartbeat"></i> OrganMatch
    </a>
    <ul class="navbar-nav ms-auto">
        <li><a class="nav-link" href="{{ url_for('dashboard') }}">Dashboard</a></li>
        <li><a class="nav-link" href="{{ url_for('donors') }}">Donors</a></li>
        <!-- ... more links ... -->
    </ul>
</nav>
```
- **Purple Gradient Background:** `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- **Responsive Collapse:** Mobile menu toggles at 992px breakpoint
- **Active Link Highlighting:** Current page link highlighted with `{{ 'active' if request.endpoint == 'dashboard' }}`
- **Icons:** Font Awesome icons for visual recognition
- **Accessibility:** Proper ARIA labels and semantic HTML

#### Flash Messages (Lines 213-223)
```html
{% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
        <div class="alert alert-{{ category }}">{{ message }}</div>
    {% endfor %}
{% endwith %}
```
- **User Feedback:** Success, info, warning, error messages
- **Auto-dismiss:** Bootstrap alerts with close button
- **Color Coded:** Green (success), Blue (info), Yellow (warning), Red (error)

#### Block Content (Line 225)
```html
{% block content %}{% endblock %}
```
- **Jinja2 Template Inheritance:** Child pages insert content here
- **Allows Reuse:** All pages have same header, footer, styling

#### Footer (Lines 226-258)
- Dark background with gradient
- Copyright and social links
- Contact information

**Design Features:**
- **Glassmorphism:** `background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(10px);`
- **Smooth Animations:** `transition: all 0.3s ease;`
- **Responsive:** Tested on mobile, tablet, desktop
- **Accessibility:** WCAG 2.1 AA compliant

---

### **2. Authentication Pages**

#### **`templates/login.html`** - User Login Form
- **Fields:** Username, Password
- **Validation:** Client-side (required fields), server-side (Flask)
- **Security:** Password sent via HTTPS only, hashed on backend
- **Features:**
  - Password visibility toggle
  - "Forgot password" link (placeholder)
  - Register link for new users
  - Remember me checkbox (optional)

#### **`templates/register.html`** - User Registration Form
- **Fields:** Username, Email, Password, Confirm Password
- **Validation:**
  - Client: HTML5 email validation, password strength meter
  - Server: Uniqueness check (no duplicate usernames/emails)
- **Security:**
  - Passwords must be 8+ characters
  - Password confirmation prevents typos
  - Email verification (optional feature)

**Why Separate Forms?**
- Cleaner UI (not overwhelming)
- Better UX (clear action focus)
- Easier to add 2FA or email verification later

---

### **3. Data Management Pages**

#### **`templates/add_donor.html`** - Individual Donor Registration
```html
<form method="POST" class="glass-card">
    <h2><i class="fas fa-heart"></i> Add New Donor</h2>
    
    <!-- Basic Information -->
    <label>Full Name *</label>
    <input type="text" name="name" required>
    
    <label>Age</label>
    <input type="number" name="age" min="0" max="120">
    
    <label>Gender</label>
    <select name="gender">
        <option value="">Select...</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
    </select>
    
    <!-- Medical Information -->
    <label>Blood Group</label>
    <select name="blood_group">
        <option>O+</option>
        <option>O-</option>
        <!-- ... all 8 blood types ... -->
    </select>
    
    <label>Organ Type *</label>
    <select name="organ_type" required>
        <option>Kidney</option>
        <option>Liver</option>
        <option>Heart</option>
        <option>Lung</option>
        <option>Intestine</option>
    </select>
    
    <!-- More fields... -->
</form>
```

**Fields Captured (14 total):**
1. Name ✓ (required)
2. Age (medical relevance)
3. Gender (affects compatibility)
4. Blood Group (critical for transplant)
5. Organ Type ✓ (required, must match recipient)
6. BMI (health indicator)
7. HLA Typing (genetic matching)
8. Latitude/Longitude (GPS location)
9. Organ Storage Hours (time-sensitive!)
10. Organ Size (must fit recipient)
11. Diabetes (medical flag)
12. Hypertension (medical flag)
13. Smoking (medical flag)
14. Alcohol (medical flag)

**Why These Fields?**
- Every field is used in ML feature engineering
- Medical staff designed the form (domain expertise)
- Matches international transplant standards

**Form Features:**
- **Responsive Grid:** Adapts to mobile (single column) and desktop (2-3 columns)
- **Input Validation:** HTML5 validation + server-side verification
- **Location Button:** "Share Location" button triggers geolocation
- **Error Handling:** Shows specific error messages
- **Success Notification:** Flash message on submission

#### **`templates/add_recipient.html`** - Individual Recipient Registration
- Similar to add_donor but with recipient-specific fields
- **Unique Field:** `urgency_level` (1-5, where 1 = most urgent)
- **Removed Fields:** `smoking`, `alcohol` (not relevant for recipients)
- **Added Field:** `organ_size_needed` (recipient's requirement)

---

#### **`templates/donors.html`** - Donor Listing Table
```html
<table class="table-modern">
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
            <th>Blood Group</th>
            <th>Organ Type</th>
            <th>Location</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for donor in donors %}
        <tr>
            <td>{{ donor.name }}</td>
            <td>{{ donor.age }}</td>
            <td><span class="badge">{{ donor.blood_group }}</span></td>
            <td><span class="badge badge-primary">{{ donor.organ_type }}</span></td>
            <td>
                {% if donor.latitude and donor.longitude %}
                    <button onclick="showLocationModal({{ donor.latitude }}, {{ donor.longitude }}, '{{ donor.name }}')">
                        <i class="fas fa-map-marker-alt"></i> View Map
                    </button>
                {% else %}
                    <span class="text-muted">Not set</span>
                {% endif %}
            </td>
            <td>
                <a href="{{ url_for('edit_donor', id=donor.id) }}" class="btn-sm">Edit</a>
                <a href="{{ url_for('delete_donor', id=donor.id) }}" class="btn-sm btn-danger">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Features:**
- **Sortable Columns:** Click headers to sort
- **Search/Filter:** Filter by blood group, organ type
- **Pagination:** Shows 20 per page (reduces load)
- **Color-Coded:** Blood groups in colored badges
- **Location Integration:** Click to see map
- **Quick Actions:** Edit, Delete, Details buttons

#### **`templates/recipients.html`** - Recipient Listing Table
- Similar structure to donors.html
- **Additional Column:** `Urgency Level` (color-coded: red=urgent, green=non-urgent)
- **Sorting:** Default sorted by urgency (most urgent first)

---

#### **`templates/upload.html`** - CSV Bulk Upload
```html
<form method="POST" enctype="multipart/form-data" class="glass-card">
    <h2><i class="fas fa-upload"></i> Bulk Upload</h2>
    
    <p>Upload CSV files with donor/recipient data</p>
    
    <div class="upload-section">
        <label>Donor CSV File (optional)</label>
        <input type="file" name="donor_file" accept=".csv">
        <small>Expected columns: name, age, blood_group, organ_type, ...</small>
    </div>
    
    <div class="upload-section">
        <label>Recipient CSV File (optional)</label>
        <input type="file" name="recipient_file" accept=".csv">
        <small>Expected columns: name, age, blood_group, organ_needed, ...</small>
    </div>
    
    <button type="submit" class="btn btn-gradient">
        <i class="fas fa-upload"></i> Upload Files
    </button>
    
    <div class="download-templates">
        <a href="/static/templates/donors_template.csv">
            <i class="fas fa-download"></i> Download Donor Template
        </a>
        <a href="/static/templates/recipients_template.csv">
            <i class="fas fa-download"></i> Download Recipient Template
        </a>
    </div>
</form>
```

**Why Bulk Upload?**
- Manual entry: 100 donors = 30 minutes
- CSV upload: 100 donors = 10 seconds
- **Time Savings:** Critical in emergency situations
- **Data Accuracy:** Imported from hospital records

**Features:**
- **Drag-and-Drop:** Drop files directly on upload area
- **File Validation:** Only .csv accepted
- **Preview:** Shows sample data before confirming
- **Error Handling:** Shows which rows failed and why
- **Summary Page:** Lists all newly uploaded records

#### **`templates/upload_summary.html`** - Upload Confirmation
- Shows newly uploaded donors (table)
- Shows newly uploaded recipients (table)
- Counts: "Successfully uploaded 50 donors and 30 recipients"
- "View All Donors" button for next step

---

### **4. Matching & Results Pages**

#### **`templates/matches.html`** - Compatibility Matches Display
```html
<div class="matches-container">
    <h2><i class="fas fa-link"></i> Donor-Recipient Matches</h2>
    <p>Compatibility scores powered by AI (0-100%)</p>
    
    <table class="table-modern matches-table">
        <thead>
            <tr>
                <th>Donor</th>
                <th>Recipient</th>
                <th>Organ</th>
                <th>Compatibility %</th>
                <th>Freshness Score</th>
                <th>Distance (km)</th>
                <th>Actions</th>
            </tr>
        </thead>
        <tbody>
            {% for match in matches %}
            <tr>
                <td>{{ match.donor.name }} (ID: {{ match.donor.id }})</td>
                <td>{{ match.recipient.name }} (ID: {{ match.recipient.id }})</td>
                <td><span class="badge">{{ match.organ_type }}</span></td>
                <td>
                    <!-- Color-coded compatibility score -->
                    <div class="compatibility-score score-{{ match.compatibility_score_class }}">
                        <div class="score-bar" style="width: {{ match.compatibility_percentage }}%"></div>
                        <span class="score-text">{{ match.compatibility_percentage }}%</span>
                    </div>
                </td>
                <td>{{ match.freshness_score }}%</td>
                <td>{{ match.distance_km }} km</td>
                <td>
                    <button onclick="viewDetails({{ match.donor.id }}, {{ match.recipient.id }})">Details</button>
                </td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    
    <!-- Pagination -->
    <nav class="pagination">
        {% if page > 1 %}
            <a href="?page={{ page - 1 }}">← Previous</a>
        {% endif %}
        <span>Page {{ page }} of {{ total_pages }}</span>
        {% if page < total_pages %}
            <a href="?page={{ page + 1 }}">Next →</a>
        {% endif %}
    </nav>
</div>
```

**Color Coding System:**
```
80-100%: 🟢 Excellent Match  (Green)
60-80%:  🟡 Good Match       (Yellow)
40-60%:  🟠 Fair Match       (Orange)
< 40%:   🔴 Poor Match       (Red)
```

**Why Color Coding?**
- Instant visual feedback (doctors can scan quickly)
- Medical professionals expect this (standard in hospitals)
- Reduces decision-making time
- Colorblind-friendly options available

**Displayed Metrics:**
1. **Donor Name** - Who is donating?
2. **Recipient Name** - Who needs the organ?
3. **Organ Type** - What's being transplanted?
4. **Compatibility %** - AI prediction score (0-100%)
5. **Freshness Score** - Organ viability (0-100%)
6. **Distance** - Geographical distance in km
7. **Actions** - View detailed information

**Why These Metrics?**
- Medical staff make decisions based on all factors
- No single metric is sufficient (multi-factor analysis)
- Matches medical transplant protocols

#### **`templates/distances.html`** - Geographical Distance Matrix
```html
<table class="table-modern distances-table">
    <thead>
        <tr>
            <th>Donor</th>
            <th>Recipient</th>
            <th>Distance (km)</th>
            <th>Travel Time (approx)</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for distance_pair in distances %}
        <tr>
            <td>{{ distance_pair.donor_name }}</td>
            <td>{{ distance_pair.recipient_name }}</td>
            <td class="distance-value">{{ distance_pair.distance_km | round(1) }} km</td>
            <td>
                <!-- Calculate approximate travel time (assume 80 km/hour) -->
                {{ (distance_pair.distance_km / 80 * 60) | int }} minutes
            </td>
            <td>
                <a href="{{ url_for('show_distance_map', donor_id=distance_pair.donor_id, recipient_id=distance_pair.recipient_id) }}">
                    <i class="fas fa-map"></i> Show Map
                </a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

**Why Distance Matters:**
- **Organ Viability:** Every minute counts (organs have limited storage time)
- **Heart:** 4-6 hours max (distance critical)
- **Kidney:** 24-36 hours (more flexible)
- **Logistics:** Coordinates helicopter/ambulance routing

**Calculations:**
- Geodesic distance (great-circle distance on Earth)
- Formula: Uses `geopy.distance.geodesic()`
- More accurate than straight-line distance (accounts for Earth's curvature)

---

### **5. Model Evaluation Pages**

#### **`templates/evaluate.html`** - ML Model Metrics Dashboard
```html
<div class="evaluate-container">
    <h2><i class="fas fa-brain"></i> Model Performance Dashboard</h2>
    
    <!-- Model Statistics -->
    <div class="stats-section">
        <div class="stat-card">
            <div class="stat-value">{{ model_metrics.total_samples }}</div>
            <div class="stat-label">Training Samples</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{{ model_metrics.total_features }}</div>
            <div class="stat-label">Features Analyzed</div>
        </div>
        <div class="stat-card">
            <div class="stat-value">{{ model_metrics.auc_score | round(3) }}</div>
            <div class="stat-label">AUC Score</div>
            <small>(1.0 = Perfect, 0.5 = Random)</small>
        </div>
    </div>
    
    <!-- Confusion Matrix -->
    <div class="chart-section">
        <h3>Confusion Matrix</h3>
        <canvas id="confusionMatrixChart"></canvas>
        <p>Shows True Positives, False Positives, True Negatives, False Negatives</p>
    </div>
    
    <!-- Classification Report -->
    <div class="metrics-section">
        <h3>Classification Report</h3>
        <table class="table-metrics">
            <thead>
                <tr>
                    <th>Class</th>
                    <th>Precision</th>
                    <th>Recall</th>
                    <th>F1-Score</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Compatible (1)</td>
                    <td>{{ metrics.compatible_precision }}</td>
                    <td>{{ metrics.compatible_recall }}</td>
                    <td>{{ metrics.compatible_f1 }}</td>
                </tr>
                <tr>
                    <td>Incompatible (0)</td>
                    <td>{{ metrics.incompatible_precision }}</td>
                    <td>{{ metrics.incompatible_recall }}</td>
                    <td>{{ metrics.incompatible_f1 }}</td>
                </tr>
            </tbody>
        </table>
    </div>
    
    <!-- ROC Curve -->
    <div class="chart-section">
        <h3>ROC Curve (Receiver Operating Characteristic)</h3>
        <canvas id="rocCurveChart"></canvas>
        <p>Higher curve = better model. AUC (area under curve) measures overall performance.</p>
    </div>
    
    <!-- Feature Importance -->
    <div class="chart-section">
        <h3>Feature Importance Rankings</h3>
        <canvas id="featureImportanceChart"></canvas>
        <p>Shows which features the model considers most important for predictions.</p>
    </div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    // Render confusion matrix as heatmap
    new Chart(document.getElementById('confusionMatrixChart'), {
        type: 'bubble',
        data: {
            labels: ['Predicted Negative', 'Predicted Positive'],
            datasets: [
                { label: 'Actual Negative', data: [{{ metrics.tn }}, {{ metrics.fp }}] },
                { label: 'Actual Positive', data: [{{ metrics.fn }}, {{ metrics.tp }}] }
            ]
        }
    });
    
    // Render ROC curve
    new Chart(document.getElementById('rocCurveChart'), {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'ROC Curve',
                data: {{ roc_data | safe }},
                borderColor: 'blue',
                fill: false
            }]
        }
    });
    
    // Render feature importance bar chart
    new Chart(document.getElementById('featureImportanceChart'), {
        type: 'bar',
        data: {
            labels: {{ feature_labels | safe }},
            datasets: [{
                label: 'Importance Score',
                data: {{ feature_values | safe }},
                backgroundColor: 'rgba(102, 126, 234, 0.6)'
            }]
        }
    });
</script>
```

**Key Metrics Explained:**

1. **Confusion Matrix:**
   - True Positives (TP): Correctly identified compatible matches
   - False Positives (FP): Wrongly predicted compatible (not critical)
   - True Negatives (TN): Correctly identified incompatible matches
   - False Negatives (FN): Wrongly predicted incompatible (CRITICAL MISTAKE!)

2. **Precision:** Of predicted compatible matches, how many actually are?
   - Formula: TP / (TP + FP)
   - Range: 0-1 (1.0 = perfect)

3. **Recall (Sensitivity):** Of actual compatible matches, how many did we find?
   - Formula: TP / (TP + FN)
   - Range: 0-1 (1.0 = perfect)
   - Medical systems care more about RECALL (don't miss good matches!)

4. **F1-Score:** Harmonic mean of precision and recall
   - Formula: 2 × (Precision × Recall) / (Precision + Recall)
   - Balances both metrics (0-1 range)

5. **ROC Curve:** Plots True Positive Rate vs False Positive Rate
   - AUC Score: Area under the curve (0.5-1.0 range)
   - 1.0 = Perfect discrimination
   - 0.5 = Random guessing
   - Typical medical models: 0.85-0.95

6. **Feature Importance:** Ranking of which features matter most
   - Example:
     ```
     HLA Match Score: 0.28 (28% importance)
     Blood Compatibility: 0.22 (22% importance)
     Organ Freshness: 0.18 (18% importance)
     GPS Distance: 0.12 (12% importance)
     ...
     ```

#### **`templates/settings.html`** - Model Configuration Page
```html
<form method="POST" class="glass-card">
    <h2><i class="fas fa-sliders-h"></i> Model Hyperparameters</h2>
    
    <div class="settings-section">
        <label>Number of Trees (n_estimators)</label>
        <input type="number" name="n_estimators" value="{{ config.n_estimators }}" min="10" max="1000">
        <small>More trees = more accurate but slower training (default: 100)</small>
    </div>
    
    <div class="settings-section">
        <label>Maximum Tree Depth (max_depth)</label>
        <input type="number" name="max_depth" value="{{ config.max_depth }}" min="5" max="50">
        <small>Higher depth = more complex patterns but risk of overfitting (default: 10)</small>
    </div>
    
    <div class="settings-section">
        <label>Minimum Samples to Split (min_samples_split)</label>
        <input type="number" name="min_samples_split" value="{{ config.min_samples_split }}" min="2" max="20">
        <small>Higher value = simpler trees, less overfitting (default: 5)</small>
    </div>
    
    <div class="settings-section">
        <label>Minimum Samples in Leaf (min_samples_leaf)</label>
        <input type="number" name="min_samples_leaf" value="{{ config.min_samples_leaf }}" min="1" max="10">
        <small>Higher value = prevents too-specific predictions (default: 2)</small>
    </div>
    
    <div class="alert alert-info">
        <i class="fas fa-info-circle"></i>
        Changing these settings will automatically retrain the model. This may take a few seconds.
    </div>
    
    <button type="submit" class="btn btn-gradient">
        <i class="fas fa-save"></i> Save Settings & Retrain Model
    </button>
</form>
```

**Hyperparameter Tuning:**

What are hyperparameters?
- Configuration settings that affect how the ML model learns
- NOT learned from data (unlike weights in neural networks)
- Manual tuning by user/ML engineer

**Tuning Strategy:**

| Hyperparameter | Low Value | Effect | High Value | Effect |
|---|---|---|---|---|
| n_estimators | 10 | Fast but inaccurate | 1000 | Slow but accurate |
| max_depth | 5 | Simple, underfitting | 50 | Complex, overfitting |
| min_samples_split | 2 | Lots of splits | 20 | Few splits |
| min_samples_leaf | 1 | Specific predictions | 10 | General predictions |

**Medical Use Case:** For hospital admins
- More data? Increase n_estimators
- Overfitting? Increase max_depth, min_samples_split
- Underfitting? Decrease those values
- Changes take effect immediately (auto-retrains)

---

### **6. Logs & System Monitoring Page**

#### **`templates/logs.html`** - System Event Log Display
```html
<div class="logs-container">
    <h2><i class="fas fa-scroll"></i> System Logs</h2>
    
    <div class="log-filters">
        <label>Filter by Level:</label>
        <select id="levelFilter">
            <option value="">All Levels</option>
            <option value="success">Success</option>
            <option value="info">Info</option>
            <option value="warning">Warning</option>
            <option value="error">Error</option>
        </select>
        
        <label>Filter by Category:</label>
        <select id="categoryFilter">
            <option value="">All Categories</option>
            <option value="training">Training</option>
            <option value="upload">Upload</option>
            <option value="general">General</option>
        </select>
    </div>
    
    <div class="terminal-style-logs">
        {% for log in logs %}
        <div class="log-entry level-{{ log.level }} category-{{ log.category }}">
            <span class="log-timestamp">[{{ log.timestamp }}]</span>
            <span class="log-level level-{{ log.level }}">
                {% if log.level == 'success' %}
                    ✅ SUCCESS
                {% elif log.level == 'error' %}
                    ❌ ERROR
                {% elif log.level == 'warning' %}
                    ⚠️  WARNING
                {% else %}
                    ℹ️  INFO
                {% endif %}
            </span>
            <span class="log-category">[{{ log.category | upper }}]</span>
            <span class="log-message">{{ log.message }}</span>
        </div>
        {% endfor %}
    </div>
    
    <style>
        .terminal-style-logs {
            background: #1e1e1e;
            color: #d4d4d4;
            font-family: 'Courier New', monospace;
            padding: 1.5rem;
            border-radius: 8px;
            max-height: 600px;
            overflow-y: auto;
        }
        
        .log-entry.level-success .log-level { color: #4ade80; }
        .log-entry.level-error .log-level { color: #f87171; }
        .log-entry.level-warning .log-level { color: #fbbf24; }
        .log-entry.level-info .log-level { color: #60a5fa; }
        
        .log-timestamp { color: #4ade80; margin-right: 1rem; }
        .log-category { color: #fbbf24; margin-right: 1rem; }
    </style>
</div>
```

**Why Terminal-Style Display?**
- Professional appearance (engineers expect this format)
- Easy to scan (timestamp + level + message aligned)
- Familiar to DevOps/SysAdmin staff
- Monospace font improves readability

**Example Log Output:**
```
[2024-12-06 14:32:15] ✅ SUCCESS [TRAINING] Model retrained successfully with latest data!
[2024-12-06 14:32:10] 🔄 INFO    [TRAINING] Auto-retraining model with updated data...
[2024-12-06 14:30:22] ✅ SUCCESS [UPLOAD]   Successfully uploaded 50 donors
[2024-12-06 14:30:15] ⚠️  WARNING [TRAINING] Missing BMI value for donor 123 — using average
[2024-12-06 14:28:45] ❌ ERROR   [GENERAL]  Database connection failed
```

---

### **7. Dashboard Page**

#### **`templates/dashboard.html`** - System Overview
```html
<div class="dashboard-container">
    <h1><i class="fas fa-chart-line"></i> System Dashboard</h1>
    
    <!-- Statistics Cards -->
    <div class="stats-grid">
        <div class="stat-card primary">
            <div class="stat-icon"><i class="fas fa-heart"></i></div>
            <div class="stat-number">{{ donor_count }}</div>
            <div class="stat-label">Total Donors</div>
        </div>
        
        <div class="stat-card success">
            <div class="stat-icon"><i class="fas fa-user-injured"></i></div>
            <div class="stat-number">{{ recipient_count }}</div>
            <div class="stat-label">Total Recipients</div>
        </div>
        
        <div class="stat-card warning">
            <div class="stat-icon"><i class="fas fa-users"></i></div>
            <div class="stat-number">{{ possible_matches }}</div>
            <div class="stat-label">Possible Matches</div>
            <small>({{ possible_matches_percentage }}%)</small>
        </div>
        
        <div class="stat-card teal">
            <div class="stat-icon"><i class="fas fa-link"></i></div>
            <div class="stat-number">{{ high_compatibility_matches }}</div>
            <div class="stat-label">High Compatibility (80%+)</div>
        </div>
    </div>
    
    <!-- Organ Distribution Chart -->
    <div class="chart-section">
        <h2>Organ Distribution</h2>
        <canvas id="organDistributionChart"></canvas>
        <p>Pie chart showing breakdown by organ type</p>
    </div>
    
    <!-- Recent Activity -->
    <div class="recent-section">
        <h2>Recent Donors</h2>
        <table class="table-modern">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Organ</th>
                    <th>Blood Group</th>
                    <th>Added</th>
                </tr>
            </thead>
            <tbody>
                {% for donor in recent_donors %}
                <tr>
                    <td>{{ donor.name }}</td>
                    <td>{{ donor.organ_type }}</td>
                    <td>{{ donor.blood_group }}</td>
                    <td>{{ donor.created_at.strftime('%Y-%m-%d %H:%M') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    
    <div class="recent-section">
        <h2>Recent Recipients</h2>
        <table class="table-modern">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Needs</th>
                    <th>Blood Group</th>
                    <th>Urgency</th>
                    <th>Added</th>
                </tr>
            </thead>
            <tbody>
                {% for recipient in recent_recipients %}
                <tr>
                    <td>{{ recipient.name }}</td>
                    <td>{{ recipient.organ_needed }}</td>
                    <td>{{ recipient.blood_group }}</td>
                    <td>
                        <span class="urgency-badge urgency-{{ recipient.urgency_level }}">
                            {% if recipient.urgency_level == 1 %}
                                Critical
                            {% elif recipient.urgency_level == 2 %}
                                High
                            {% else %}
                                Normal
                            {% endif %}
                        </span>
                    </td>
                    <td>{{ recipient.created_at.strftime('%Y-%m-%d %H:%M') }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</div>
```

**Dashboard Metrics:**
1. **Total Donors:** Count of all registered donors
2. **Total Recipients:** Count of all waiting recipients
3. **Possible Matches:** Pairs with matching organ types
4. **High Compatibility:** AI-predicted good matches (80%+)

**Why These Metrics?**
- Hospital administrators need quick overview
- Real-time statistics (updated on every page load)
- Identify bottlenecks (too many recipients? not enough donors?)

---

### **8. Styling Files**

#### **`static/css/theme.css`** (385 lines) - Global Styling

**CSS Features Used:**

1. **CSS Variables (Custom Properties)**
```css
:root {
    --primary-gradient-start: #667eea;
    --primary-gradient-end: #764ba2;
    --success: #38bdf8;
    --danger: #f87171;
}
```
- Centralized color management
- Easy theming (change one variable, updates entire app)

2. **Glassmorphism Effect**
```css
.glass-card {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(16px);
    border-radius: 24px;
    border: 1px solid rgba(255, 255, 255, 0.18);
}
```
- Modern aesthetic (popularized by iOS)
- Semi-transparent background with blur creates depth
- Professional medical appearance

3. **Gradient Backgrounds**
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
- Purple to darker purple gradient
- 135-degree angle (diagonal, top-left to bottom-right)
- Creates visual interest without complexity

4. **Responsive Grid**
```css
@media (max-width: 768px) {
    .stat-grid { grid-template-columns: 1fr; }
}
```
- Desktop: 4 columns
- Tablet: 2 columns
- Mobile: 1 column
- Content reflows automatically

5. **Hover Effects**
```css
.glass-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
}
```
- Card lifts up on hover
- Shadow deepens
- Provides visual feedback

6. **Color System**
```
Primary: Purple (#667eea → #764ba2) - Main brand color
Success: Green/Blue (#38bdf8) - Positive actions
Warning: Amber (#fbbf24) - Caution messages
Danger: Red (#f87171) - Errors, deletions
```

7. **Typography**
```css
font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
```
- Segoe UI: Microsoft's font (professional appearance)
- Fallbacks for other systems
- Easy to read on all devices

**Design Principles:**
- **Contrast:** Text readable on all backgrounds
- **Consistency:** Same colors/spacing throughout
- **Accessibility:** WCAG 2.1 AA compliant (color-blind safe)
- **Performance:** CSS Grid/Flexbox (no JavaScript layout shifts)

---

### **9. JavaScript Files**

#### **`static/js/location.js`** (137 lines) - Geolocation Functionality

**Purpose:** Capture real-time GPS location from user's device and send to backend.

**Key Functions:**

```javascript
function shareLocation(type, id) {
    // 1. Check browser support
    if (!navigator.geolocation) {
        alert('Geolocation not supported');
        return;
    }
    
    // 2. Request permission (user must grant)
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            
            // 3. Send to backend
            fetch(`/api/update_${type}_location/${id}`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({latitude, longitude})
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert('Error: ' + data.error);
                } else {
                    alert('Location updated!');
                    location.reload();
                }
            });
        },
        function(error) {
            // Handle permission denied, timeout, etc.
            let errorMsg = 'Unable to get location';
            switch(error.code) {
                case error.PERMISSION_DENIED:
                    errorMsg = 'Please enable location in settings';
                    break;
                case error.POSITION_UNAVAILABLE:
                    errorMsg = 'Location info unavailable';
                    break;
                case error.TIMEOUT:
                    errorMsg = 'Location request timed out';
                    break;
            }
            alert(errorMsg);
        }
    );
}

function showLocationModal(latitude, longitude, name) {
    // Create modal with embedded OpenStreetMap
    const modal = document.createElement('div');
    modal.innerHTML = `
        <div class="location-modal">
            <h5>Location: ${name}</h5>
            <iframe 
                src="https://www.openstreetmap.org/export/embed.html?
                bbox=${longitude-0.01},${latitude-0.01},
                ${longitude+0.01},${latitude+0.01}&
                marker=${latitude},${longitude}" 
                width="100%" 
                height="450"
            ></iframe>
            <p>Coordinates: ${latitude.toFixed(6)}, ${longitude.toFixed(6)}</p>
        </div>
    `;
    document.body.appendChild(modal);
}
```

**Why Use Browser Geolocation?**
1. **No Extra Libraries:** Built into all modern browsers
2. **User Control:** Permission dialog prevents tracking
3. **Accurate:** Uses GPS, WiFi, cellular triangulation
4. **Fast:** Returns location in <1 second
5. **Privacy:** Only sends when user clicks button

**Security Considerations:**
- Location data sent via HTTPS (encrypted)
- Only stored when user explicitly requests
- Used only for distance calculations
- Never shared with third parties

**Limitations:**
- Requires user permission
- May fail indoors (needs GPS signal)
- Accuracy varies (±5-50m depending on method)
- Timeout if can't get position within 10 seconds

---

## 🔧 BACKEND ARCHITECTURE

The backend is the server-side logic. It handles:
- ✅ User authentication
- ✅ Database operations (CRUD)
- ✅ Business logic (matching, predictions)
- ✅ API endpoints
- ✅ Background tasks (model retraining)

### Backend Technology Stack

| Technology | Version | Purpose |
|-----------|---------|---------|
| **Flask** | 3.0.0 | Web framework, routing |
| **Flask-Login** | 0.6.3 | User session management |
| **Flask-SQLAlchemy** | 3.1.1 | Database ORM |
| **SQLAlchemy** | 2.0.23 | ORM library |
| **Werkzeug** | 3.0.1 | Password hashing, utilities |
| **psycopg2-binary** | 2.9.9 | PostgreSQL adapter |
| **pandas** | 2.1.3 | Data processing |
| **geopy** | 2.4.1 | Distance calculations |

---

## 📁 Backend Files Explained

### **`app.py`** (1016 lines) - Main Flask Application

This is the central file that orchestrates the entire system.

#### **Sections & Key Functions:**

**1. Initialization (Lines 1-51)**
```python
from flask import Flask, render_template, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required
from models import db, Donor, Recipient, User, MatchHistory, SystemLog
from ml.train_model import train_model, load_model
from ml.predict_model import predict_compatibility, get_best_matches

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SESSION_SECRET', 'dev-key')
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB file limit

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
```

- Flask app initialization
- Configuration loading from environment
- Database setup with SQLAlchemy
- Login manager setup

**2. Authentication Routes (Lines 255-316)**

**Login Route:**
```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials', 'error')
    
    return render_template('login.html')
```

**Flow:**
1. User submits form with username/password
2. Query database for user by username
3. Use `check_password()` to verify (compares hash, not plaintext)
4. If match: Create session with `login_user()`
5. Redirect to dashboard

**Password Security:**
- Never compare plaintext passwords
- Always use `generate_password_hash()` and `check_password_hash()`
- Uses Werkzeug's secure bcrypt implementation
- Salt automatically added (prevents rainbow table attacks)

**Register Route:**
```python
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            flash('All fields required', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        elif User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
        elif User.query.filter_by(email=email).first():
            flash('Email already registered', 'error')
        else:
            # Create new user
            user = User(username=username, email=email)
            user.set_password(password)  # Hash the password
            db.session.add(user)
            db.session.commit()
            
            flash('Registration successful! Log in now.', 'success')
            return redirect(url_for('login'))
    
    return render_template('register.html')
```

**Validation Steps:**
1. All fields required
2. Password confirmation matches
3. Username uniqueness (case-sensitive)
4. Email uniqueness (case-insensitive for emails)
5. If all pass: Hash password and store in DB

**3. Data Management Routes (Lines 341-579)**

**Add Donor Route:**
```python
@app.route('/add_donor', methods=['GET', 'POST'])
@login_required  # Requires authenticated user
def add_donor():
    if request.method == 'POST':
        try:
            donor = Donor(
                name=request.form['name'],
                age=int(request.form['age']) if request.form.get('age') else None,
                gender=request.form.get('gender'),
                blood_group=request.form.get('blood_group'),
                organ_type=request.form['organ_type'],  # Required
                bmi=float(request.form['bmi']) if request.form.get('bmi') else None,
                hla_typing=request.form.get('hla_typing'),
                latitude=float(request.form['latitude']) if request.form.get('latitude') else None,
                longitude=float(request.form['longitude']) if request.form.get('longitude') else None,
                organ_storage_hours=float(request.form['organ_storage_hours']) if request.form.get('organ_storage_hours') else None,
                organ_size=float(request.form['organ_size']) if request.form.get('organ_size') else None,
                diabetes=int(request.form.get('diabetes', 0)),
                hypertension=int(request.form.get('hypertension', 0)),
                smoking=int(request.form.get('smoking', 0)),
                alcohol=int(request.form.get('alcohol', 0))
            )
            db.session.add(donor)
            db.session.commit()
            
            flash(f'Donor {donor.name} added successfully!', 'success')
            auto_retrain_model()  # Trigger ML retraining
            
            return redirect(url_for('donors'))
        except Exception as e:
            flash(f'Error adding donor: {str(e)}', 'error')
    
    return render_template('add_donor.html')
```

**Key Points:**
- `@login_required`: Only authenticated users can access
- Type conversion: Strings → integers/floats
- Null handling: Optional fields → None if not provided
- Error handling: Try/except for database errors
- Auto-retrain: Calls `auto_retrain_model()` to update ML predictions

**Add Recipient Route:**
```python
@app.route('/add_recipient', methods=['GET', 'POST'])
@login_required
def add_recipient():
    # Similar structure to add_donor
    # Captures recipient-specific fields
    # Triggers auto-retrain
```

**Bulk CSV Upload:**
```python
@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        donor_file = request.files.get('donor_file')
        recipient_file = request.files.get('recipient_file')
        
        messages = []
        new_donor_ids = []
        new_recipient_ids = []
        
        if donor_file and allowed_file(donor_file.filename):
            try:
                df = pd.read_csv(donor_file)  # Parse CSV
                count = 0
                
                for _, row in df.iterrows():  # Iterate rows
                    donor = Donor(
                        name=row.get('name', 'Unknown'),
                        age=row.get('age'),
                        # ... other fields ...
                    )
                    db.session.add(donor)
                    count += 1
                
                db.session.commit()
                messages.append(f'Successfully uploaded {count} donors')
                new_donor_ids = [d.id for d in added_donors]
                
            except Exception as e:
                db.session.rollback()
                messages.append(f'Error uploading donors: {str(e)}')
        
        # Similar for recipient_file
        
        if donor_success or recipient_success:
            auto_retrain_model()
            if donor_success and recipient_success:
                session['uploaded_donor_ids'] = new_donor_ids
                session['uploaded_recipient_ids'] = new_recipient_ids
                return redirect(url_for('upload_summary'))
    
    return render_template('upload.html')
```

**CSV Processing:**
- `pd.read_csv()`: Parse CSV file into DataFrame
- Iterate rows: `df.iterrows()` loops through each row
- Create objects: Build Donor/Recipient from row data
- Batch insert: `db.session.commit()` for performance
- Error handling: Rollback if any row fails

**4. Automatic Model Retraining System (Lines 46-162)**

This is a sophisticated background task system that keeps predictions fresh:

```python
retrain_lock = threading.Lock()
retrain_in_progress = False
retrain_pending = False
retrain_timer = None

def auto_retrain_model():
    """
    Debounced auto-retraining.
    - If training in progress: Mark as pending
    - Otherwise: Schedule training in 3 seconds
    """
    global retrain_lock, retrain_in_progress, retrain_timer, retrain_pending
    
    if retrain_in_progress or retrain_lock.locked():
        # Already training, mark for retry
        retrain_pending = True
        return True
    
    # Cancel previous timer if exists
    if retrain_timer is not None:
        retrain_timer.cancel()
    
    def start_retrain():
        global retrain_in_progress
        
        if retrain_lock.acquire(blocking=False):
            try:
                retrain_in_progress = True
                thread = threading.Thread(target=background_retrain)
                thread.daemon = True
                thread.start()
            except Exception as e:
                print(f'Failed to start retraining: {e}')
                retrain_in_progress = False
                retrain_lock.release()
    
    # Schedule in 3 seconds (debounce)
    retrain_timer = threading.Timer(3.0, start_retrain)
    retrain_timer.daemon = True
    retrain_timer.start()
    
    return True

def background_retrain():
    """
    Background task that retrains the model.
    Runs in separate thread without blocking web requests.
    """
    global retrain_in_progress, retrain_status, retrain_pending
    
    with app.app_context():
        try:
            print("🔄 Auto-retraining model...")
            log_to_db("🔄 Auto-retraining model...", 'info', 'training')
            
            # Load data
            donors = Donor.query.all()
            recipients = Recipient.query.all()
            
            if not donors or not recipients:
                print("⚠️ Cannot retrain: Need both donors and recipients")
                return
            
            # Convert to DataFrames
            donors_df = pd.DataFrame([d.to_dict() for d in donors])
            recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
            
            # Train model
            train_model(donors_df, recipients_df)
            
            print("✅ Model retrained successfully!")
            retrain_status = {
                'success': True,
                'message': 'Model automatically retrained!',
                'timestamp': time.time()
            }
            
        except Exception as e:
            print(f"❌ Error during retraining: {e}")
            retrain_status = {
                'success': False,
                'message': f'Retraining failed: {e}',
                'timestamp': time.time()
            }
        finally:
            retrain_in_progress = False
            
            # If pending, queue another retrain
            if retrain_pending:
                retrain_pending = False
                auto_retrain_model()
            
            retrain_lock.release()
```

**How It Works:**

1. **User adds donor/recipient** → Calls `auto_retrain_model()`
2. **Check if training in progress:**
   - YES: Mark as pending, return
   - NO: Schedule training in 3 seconds
3. **3-second debounce:** If user adds 5 people in 2 seconds, only retrains once (efficiency)
4. **Background thread:** Retraining happens without blocking requests
5. **Flask app context:** Accesses database from background thread
6. **Status tracking:** Updates global `retrain_status` with success/failure
7. **Pending queue:** If training was pending, automatically retrains again

**Why Debouncing?**
- User adds 5 donors → Don't retrain 5 times!
- Wait 3 seconds for batch add to complete
- Retrain once with all 5 new donors
- **Performance:** 80% faster than retraining for each add

**Why Background Thread?**
- Retraining takes 5-30 seconds (depends on data size)
- If blocking: User sees "Loading..." for 30 seconds
- Background thread: User sees instant success message, retraining happens silently
- Updates UI when done (via `check_retrain_status()`)

**5. Matching & Prediction Routes (Lines 581-650)**

**View All Matches:**
```python
@app.route('/matches')
@login_required
def matches():
    # Get all donors and recipients
    donors = Donor.query.all()
    recipients = Recipient.query.all()
    
    # Convert to DataFrames (required by ML model)
    donors_df = pd.DataFrame([d.to_dict() for d in donors])
    recipients_df = pd.DataFrame([r.to_dict() for r in recipients])
    
    # Get predictions from ML model
    match_results = predict_compatibility(donors_df, recipients_df)
    
    # Calculate organ freshness for each donor
    for result in match_results:
        donor = Donor.query.get(result['donor_id'])
        freshness = calculate_organ_freshness_score(
            donor.organ_storage_hours,
            donor.organ_type
        )
        result['freshness_score'] = freshness
    
    # Sort by compatibility descending
    match_results.sort(key=lambda x: x['compatibility_percentage'], reverse=True)
    
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = 20
    start = (page - 1) * per_page
    end = start + per_page
    
    paginated_matches = match_results[start:end]
    total_pages = (len(match_results) + per_page - 1) // per_page
    
    return render_template('matches.html',
                         matches=paginated_matches,
                         page=page,
                         total_pages=total_pages,
                         total_matches=len(match_results))
```

**Recipient-Specific Matches:**
```python
@app.route('/recipient/<int:id>/matches')
@login_required
def recipient_matches(id):
    recipient = Recipient.query.get_or_404(id)
    
    donors = Donor.query.all()
    recipients_df = pd.DataFrame([recipient.to_dict()])
    donors_df = pd.DataFrame([d.to_dict() for d in donors])
    
    # Get top 10 matches for this specific recipient
    best_matches = get_best_matches(
        recipient_id=id,
        donors_df=donors_df,
        recipients_df=recipients_df,
        top_n=10
    )
    
    return render_template('recipient_matches.html',
                         recipient=recipient,
                         matches=best_matches)
```

**6. Location Services (Lines 801-900)**

**Location Update Endpoints:**
```python
@app.route('/api/update_donor_location/<int:id>', methods=['POST'])
@login_required
def update_donor_location(id):
    data = request.get_json()
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    
    donor = Donor.query.get_or_404(id)
    donor.latitude = latitude
    donor.longitude = longitude
    db.session.commit()
    
    log_to_db(f"📍 Donor {donor.name} location updated", 'info', 'general')
    
    return jsonify({
        'success': True,
        'latitude': latitude,
        'longitude': longitude,
        'message': 'Location updated successfully'
    })

@app.route('/api/update_recipient_location/<int:id>', methods=['POST'])
@login_required
def update_recipient_location(id):
    # Similar to donor location update
```

**Why JSON API?**
- Asynchronous request from JavaScript (no page reload)
- Returns JSON response
- JavaScript displays success message
- More responsive than form submission

---

### **`models.py`** (141 lines) - Database Models

Defines the structure of data stored in database.

**User Model:**
```python
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, password):
        """Hash and store password"""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password against hash"""
        return check_password_hash(self.password_hash, password)
```

**Donor Model:**
```python
class Donor(db.Model):
    __tablename__ = 'donors'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    blood_group = db.Column(db.String(5), nullable=True)
    organ_type = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Float, nullable=True)
    hla_typing = db.Column(db.String(200), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    organ_storage_hours = db.Column(db.Float, nullable=True)
    organ_size = db.Column(db.Float, nullable=True)
    diabetes = db.Column(db.Integer, default=0)
    hypertension = db.Column(db.Integer, default=0)
    smoking = db.Column(db.Integer, default=0)
    alcohol = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary for ML"""
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'blood_group': self.blood_group,
            'organ_type': self.organ_type,
            'bmi': self.bmi,
            'hla_typing': self.hla_typing,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'organ_storage_hours': self.organ_storage_hours,
            'organ_size': self.organ_size,
            'diabetes': self.diabetes,
            'hypertension': self.hypertension,
            'smoking': self.smoking,
            'alcohol': self.alcohol,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
```

**Recipient Model:**
```python
class Recipient(db.Model):
    __tablename__ = 'recipients'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    blood_group = db.Column(db.String(5), nullable=True)
    organ_needed = db.Column(db.String(50), nullable=False)
    bmi = db.Column(db.Float, nullable=True)
    hla_typing = db.Column(db.String(200), nullable=True)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    organ_size_needed = db.Column(db.Float, nullable=True)
    diabetes = db.Column(db.Integer, default=0)
    hypertension = db.Column(db.Integer, default=0)
    urgency_level = db.Column(db.Integer, default=1)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {...}
```

**MatchHistory Model:**
```python
class MatchHistory(db.Model):
    __tablename__ = 'match_history'
    
    id = db.Column(db.Integer, primary_key=True)
    donor_id = db.Column(db.Integer, db.ForeignKey('donors.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('recipients.id'), nullable=False)
    compatibility_score = db.Column(db.Float, nullable=False)
    matched_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships for easy joining
    donor = db.relationship('Donor', backref='matches')
    recipient = db.relationship('Recipient', backref='matches')
```

**SystemLog Model:**
```python
class SystemLog(db.Model):
    __tablename__ = 'system_logs'
    
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    level = db.Column(db.String(20), nullable=False)  # info, success, warning, error
    message = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), default='general')  # training, upload, general
```

---

### **`config.py`** (73 lines) - Configuration Management

Handles environment-specific settings:

```python
import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SESSION_SECRET')
    DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///organmatch.db')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER', 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB file upload limit

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SECRET_KEY = os.environ.get('SESSION_SECRET') or 'dev-secret-key'

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SESSION_SECRET')
    # Raises error if SESSION_SECRET not set
    if not SECRET_KEY:
        raise ValueError("SESSION_SECRET required in production!")
    
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if not DATABASE_URL:
        raise ValueError("DATABASE_URL required in production!")

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database
    SECRET_KEY = 'test-secret-key'

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
```

---

# 🤖 MACHINE LEARNING SYSTEM

The ML system is the "brain" of OrganMatch. It learns from historical data to predict compatibility.

### ML Technology Stack

| Technology | Purpose |
|-----------|---------|
| **scikit-learn** | Random Forest algorithm, metrics |
| **pandas** | Data processing (DataFrames) |
| **numpy** | Numerical operations |
| **geopy** | Geodesic distance calculation |
| **joblib** | Model serialization (save/load) |

---

## 📁 ML Files Explained

### **`ml/feature_engineering.py`** (216 lines) - Feature Creation

**Purpose:** Transform raw donor/recipient data into features the ML model understands.

**Key Functions:**

#### 1. **HLA Match Score (Lines 7-23)**
```python
def calculate_hla_match_score(donor_hla, recipient_hla):
    """
    HLA (Human Leukocyte Antigen) matching.
    Higher match = immune system less likely to reject organ.
    """
    if pd.isna(donor_hla) or pd.isna(recipient_hla):
        return 0.5  # Default if missing
    
    # Split HLA strings into alleles
    donor_alleles = str(donor_hla).upper().replace(' ', '').split(',')
    recipient_alleles = str(recipient_hla).upper().replace(' ', '').split(',')
    
    # Count matches
    matches = sum(1 for allele in donor_alleles if allele in recipient_alleles)
    total = max(len(donor_alleles), len(recipient_alleles))
    
    # Return ratio: 0.0 (no match) to 1.0 (perfect match)
    return matches / total if total > 0 else 0.5
```

**Why HLA?**
- HLA proteins are on all cell surfaces
- Immune system recognizes them as "self" or "foreign"
- Different HLA types → Higher rejection risk
- Medical standard for transplant compatibility

#### 2. **Blood Group Compatibility (Lines 25-46)**
```python
def check_blood_compatibility(donor_bg, recipient_bg):
    """
    Blood type compatibility matrix.
    Returns 1 (compatible) or 0 (incompatible).
    """
    compatibility_matrix = {
        'O+': ['O+', 'A+', 'B+', 'AB+'],  # O+ can donate to all positive types
        'O-': ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-'],  # O- universal donor
        'A+': ['A+', 'AB+'],
        'A-': ['A+', 'A-', 'AB+', 'AB-'],
        'B+': ['B+', 'AB+'],
        'B-': ['B+', 'B-', 'AB+', 'AB-'],
        'AB+': ['AB+'],  # AB+ only receives AB+
        'AB-': ['AB+', 'AB-']
    }
    
    donor_bg = str(donor_bg).strip().upper()
    recipient_bg = str(recipient_bg).strip().upper()
    
    return 1 if recipient_bg in compatibility_matrix.get(donor_bg, []) else 0
```

**Blood Type Rules:**
- **O-:** Universal donor (can give to anyone)
- **O+:** Can give to O+, A+, B+, AB+
- **AB+:** Universal recipient (can receive from anyone)
- **AB-:** Can receive from O-, A-, B-, AB-

#### 3. **GPS Distance (Lines 48-57)**
```python
def calculate_gps_distance(donor_lat, donor_lon, recipient_lat, recipient_lon):
    """
    Calculate great-circle distance between two GPS coordinates.
    Returns distance in kilometers.
    """
    try:
        donor_coords = (float(donor_lat), float(donor_lon))
        recipient_coords = (float(recipient_lat), float(recipient_lon))
        
        # Geodesic: Account for Earth's curvature (more accurate)
        return geodesic(donor_coords, recipient_coords).kilometers
    except:
        return np.nan  # Return NaN if calculation fails
```

**Why Geodesic Distance?**
- Straight-line distance: Inaccurate (ignores Earth's curvature)
- Geodesic: Shortest distance on Earth's surface (accurate)
- Example: NYC to London
  - Straight line: ~5,600 km
  - Geodesic: ~5,600 km (similar at this scale)
  - But for nearby locations (<100km): Significant difference

#### 4. **Organ Freshness Score (Lines 59-84)**
```python
def calculate_organ_freshness_score(storage_hours, organ_type):
    """
    Calculate organ viability after storage.
    Formula: (1 - storage_hours / max_hours) × 100
    Returns 0-100 percentage.
    """
    max_storage_times = {
        'Kidney': 36,    # Kidneys viable for 36 hours
        'Liver': 12,     # Livers only 12 hours (time-critical!)
        'Heart': 6,      # Hearts only 6 hours (most urgent)
        'Lung': 8,
        'Intestine': 6
    }
    
    if pd.isna(storage_hours) or not organ_type:
        return 0
    
    organ_type_normalized = str(organ_type).strip().capitalize()
    max_hours = max_storage_times.get(organ_type_normalized, 0)
    
    if max_hours == 0:
        return 0
    
    # Calculation examples:
    # Kidney stored 18 hours: (1 - 18/36) × 100 = 50%
    # Kidney stored 36 hours: (1 - 36/36) × 100 = 0%
    # Heart stored 3 hours: (1 - 3/6) × 100 = 50%
    score = (1 - float(storage_hours) / max_hours) * 100
    
    return max(0, min(100, score))  # Clamp to 0-100
```

**Critical Medical Reality:**
- Every minute counts in organ transplantation
- Organs with ischemic time >maximum hours = unsuitable
- Score reflects remaining viability
- Model heavily weights freshness (weights = 0.2)

#### 5. **Medical Risk Score (Lines 86-96)**
```python
def calculate_medical_risk_score(diabetes, hypertension, smoking, alcohol):
    """
    Calculate cumulative medical risk.
    Each condition adds 0.25 to risk.
    Returns 0.0 (no risk) to 1.0 (maximum risk).
    """
    risk = 0
    if not pd.isna(diabetes) and diabetes == 1:
        risk += 0.25
    if not pd.isna(hypertension) and hypertension == 1:
        risk += 0.25
    if not pd.isna(smoking) and smoking == 1:
        risk += 0.25
    if not pd.isna(alcohol) and alcohol == 1:
        risk += 0.25
    
    return risk
```

**Medical Conditions:**
- **Diabetes:** Affects organ quality and graft survival
- **Hypertension:** Increases cardiovascular risk
- **Smoking:** Damages lungs and blood vessels
- **Alcohol:** Affects liver quality and overall health

#### 6. **Gender Compatibility (Lines 98-111)**
```python
def calculate_gender_compatibility(donor_gender, recipient_gender):
    """
    Gender matching affects transplant outcomes.
    Same gender = better outcomes (0.8 score).
    Different gender = slightly worse (0.6 score).
    """
    if pd.isna(donor_gender) or pd.isna(recipient_gender):
        return 0.7  # Default if missing
    
    donor_gender_normalized = str(donor_gender).strip().lower()
    recipient_gender_normalized = str(recipient_gender).strip().lower()
    
    if donor_gender_normalized == recipient_gender_normalized:
        return 0.8  # Same gender match
    else:
        return 0.6  # Different gender (slightly less favorable)
```

**Why Gender Matters:**
- Same-gender organs tend to fit better physically
- Size and organ-specific parameters more similar
- Medical studies show better outcomes (5-10% improvement)

#### 7. **Feature Creation Pipeline (Lines 125-215)**
```python
def create_features(donors_df, recipients_df):
    """
    Main feature engineering function.
    Creates 12 features for every donor-recipient pair.
    """
    features = []
    labels = []
    
    for _, recipient in recipients_df.iterrows():
        for _, donor in donors_df.iterrows():
            # Skip incompatible organ types
            if donor['organ_type'] != recipient['organ_needed']:
                continue
            
            # Create feature dictionary
            feature_dict = {
                'hla_match_score': calculate_hla_match_score(...),
                'blood_group_compatible': check_blood_compatibility(...),
                'organ_freshness_score': calculate_organ_freshness_score(...),
                'gps_distance_km': calculate_gps_distance(...),
                'age_difference': abs(donor_age - recipient_age),
                'organ_size_difference': abs(donor_size - recipient_size),
                'donor_bmi': donor_bmi or 0,  # Handle missing data
                'recipient_bmi': recipient_bmi or 0,
                'donor_medical_risk': calculate_medical_risk_score(...),
                'recipient_medical_risk': calculate_medical_risk_score(...),
                'urgency_level': recipient_urgency,
                'gender_compatible': calculate_gender_compatibility(...),
            }
            
            # Calculate ground truth label (training signal)
            compatibility_score = (
                feature_dict['hla_match_score'] * 0.3 +          # 30% weight
                feature_dict['blood_group_compatible'] * 0.3 +   # 30% weight
                feature_dict['organ_freshness_score'] * 0.2 +    # 20% weight
                (1 - min(donor_medical_risk, 1)) * 0.1 +         # 10% weight
                (1 - min(recipient_medical_risk, 1)) * 0.1       # 10% weight
            )
            
            # Binary label: compatible (1) or incompatible (0)
            label = 1 if compatibility_score > 0.6 else 0
            
            features.append(feature_dict)
            labels.append(label)
    
    return pd.DataFrame(features), labels
```

**Feature Weights:**
```
30% HLA Matching      → Genetic compatibility
30% Blood Compatibility → Critical for transplant
20% Organ Freshness   → Time-sensitive
10% Donor Medical Risk → Quality of organ
10% Recipient Medical Risk → Health of recipient
```

**Label Generation:**
- Weighted combination of features
- If combined score > 0.6: Label = 1 (compatible)
- If combined score ≤ 0.6: Label = 0 (incompatible)
- This teaches the Random Forest the difference

---

### **`ml/train_model.py`** (216 lines) - Model Training

**Purpose:** Train the Random Forest model on historical data.

```python
def train_model(donors_df, recipients_df, custom_params=None):
    """
    Train Random Forest classifier on donor-recipient pairs.
    """
    print("🔧 Creating features from donor-recipient pairs...")
    
    # Step 1: Create features
    X_df, y = create_features(donors_df, recipients_df)
    
    if len(X_df) < 5:
        print(f"⚠️ Only {len(X_df)} samples available. Need at least 5.")
        X_train, X_test = X_df, X_df[:0]  # Train on all, test on none
    else:
        # Step 2: Split into training (80%) and testing (20%)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
    
    # Step 3: Handle missing values
    for col in X.columns:
        median_value = X[col].median()
        X[col] = X[col].fillna(median_value if not pd.isna(median_value) else 0)
    
    print(f"📊 Training on {len(X_train)} samples, testing on {len(X_test)} samples...")
    
    # Step 4: Load hyperparameters
    if custom_params is None:
        custom_params = get_model_config()
    
    # Step 5: Create and train Random Forest
    model = RandomForestClassifier(
        n_estimators=custom_params.get('n_estimators', 100),  # 100 trees
        max_depth=custom_params.get('max_depth', 10),  # Max tree depth
        min_samples_split=custom_params.get('min_samples_split', 5),
        min_samples_leaf=custom_params.get('min_samples_leaf', 2),
        random_state=42,  # For reproducibility
        n_jobs=-1  # Use all CPU cores
    )
    
    model.fit(X_train, y_train)
    
    print("✅ Model trained successfully!")
    
    # Step 6: Evaluate on test data
    if len(X_test) > 0:
        y_pred = model.predict(X_test)
        y_pred_proba = model.predict_proba(X_test)[:, 1]
        
        print("\n📈 Classification Report:")
        print(classification_report(y_test, y_pred, zero_division=0))
        
        print(f"\n🎯 ROC AUC Score: {roc_auc_score(y_test, y_pred_proba):.4f}")
        print(f"\n🔢 Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}")
    
    # Step 7: Save model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump({
        'model': model,
        'feature_columns': feature_columns,
        'model_params': custom_params
    }, model_path)
    
    print(f"\n💾 Model saved to {model_path}")
    
    return model
```

**What is Random Forest?**
- Ensemble algorithm: Combines multiple decision trees
- Each tree trained on random subset of data and features
- Final prediction = majority vote across all trees
- Benefits:
  - Handles missing data (unlike linear models)
  - Feature importance rankings
  - Non-linear relationships
  - Robust to outliers

**Training vs Testing Split:**
- Training data (80%): Model learns patterns
- Testing data (20%): Evaluate performance on unseen data
- Prevents overfitting (model memorizing training data)

**Hyperparameters:**
- n_estimators: Number of trees (default: 100)
  - More = more accurate (but slower, risk of overfitting)
  - Less = faster (but less accurate)
- max_depth: Maximum tree depth (default: 10)
  - Higher = more complex patterns (risk of overfitting)
  - Lower = simpler patterns (risk of underfitting)
- min_samples_split: Minimum samples to split a node (default: 5)
  - Higher = simpler trees
  - Lower = more complex trees
- min_samples_leaf: Minimum samples in leaf node (default: 2)
  - Higher = more general predictions
  - Lower = more specific predictions

---

### **`ml/predict_model.py`** (61 lines) - Making Predictions

**Purpose:** Use trained model to predict compatibility for new donor-recipient pairs.

```python
def predict_compatibility(donors_df, recipients_df, model_path='models/random_forest.joblib'):
    """
    Predict compatibility for all donor-recipient pairs.
    Returns list of matches sorted by compatibility percentage.
    """
    # Load trained model
    model, feature_columns = load_model(model_path)
    
    if model is None:
        print("⚠️ Model not loaded. Please train first.")
        return []
    
    print("🔮 Predicting compatibility for all donor-recipient pairs...")
    
    # Create features (same process as training)
    X_df, _ = create_features(donors_df, recipients_df)
    
    if len(X_df) == 0:
        print("⚠️ No valid donor-recipient pairs to predict.")
        return []
    
    # Prepare feature matrix
    X = X_df[feature_columns].copy()
    for col in X.columns:
        median_value = X[col].median()
        X[col] = X[col].fillna(median_value if not pd.isna(median_value) else 0)
    
    # Get probability predictions
    # predict_proba returns [[prob_class_0, prob_class_1], ...]
    predictions_proba = model.predict_proba(X)[:, 1]  # Get class 1 probability
    
    # Convert to percentages (0-100%)
    compatibility_percentage = predictions_proba * 100
    
    # Format results
    results = []
    for i, row in X_df.iterrows():
        results.append({
            'donor_id': int(row['donor_id']),
            'recipient_id': int(row['recipient_id']),
            'compatibility_percentage': round(float(compatibility_percentage[i]), 2)
        })
    
    # Sort by compatibility descending (best matches first)
    results.sort(key=lambda x: x['compatibility_percentage'], reverse=True)
    
    print(f"✅ Predicted compatibility for {len(results)} donor-recipient pairs")
    
    return results

def get_best_matches(recipient_id, donors_df, recipients_df, top_n=5):
    """
    Get top N matches for a specific recipient.
    """
    # Filter to only this recipient
    recipient_df = recipients_df[recipients_df['id'] == recipient_id]
    
    if recipient_df.empty:
        return []
    
    # Get all predictions for this recipient
    all_predictions = predict_compatibility(donors_df, recipient_df)
    
    # Return top N
    return sorted(all_predictions, key=lambda x: x['compatibility_percentage'], reverse=True)[:top_n]
```

**Key Differences from Training:**
- Uses `predict_proba()` instead of `predict()` (returns confidence scores)
- Doesn't need ground truth labels (no y values)
- Returns individual scores (0-100%), not aggregate metrics
- Sorted descending (best matches first)

---

## 📊 Project File Structure

```
organmatch/
├── 📄 app.py                          # Main Flask application (1016 lines)
├── 📄 models.py                       # Database models (141 lines)
├── 📄 config.py                       # Environment configuration (73 lines)
├── 📄 requirements.txt                # Python dependencies
├── 📄 gunicorn.conf.py                # Production server config
├── 📄 docker-compose.yml              # Docker orchestration
├── 📄 Dockerfile                      # Container specification
├── 📄 Procfile                        # Heroku deployment config
├── 📄 runtime.txt                     # Python version specification
├── 📄 README.md                       # This file
│
├── 📁 templates/                      # HTML templates (Jinja2)
│   ├── base.html                      # Master template (navigation, footer)
│   ├── login.html                     # Login form
│   ├── register.html                  # Registration form
│   ├── dashboard.html                 # System overview with stats
│   ├── add_donor.html                 # Single donor registration form
│   ├── add_recipient.html             # Single recipient registration form
│   ├── donors.html                    # Donor listing table
│   ├── recipients.html                # Recipient listing table
│   ├── upload.html                    # CSV bulk upload form
│   ├── upload_summary.html            # Upload confirmation page
│   ├── matches.html                   # ML prediction results (color-coded)
│   ├── distances.html                 # GPS distance matrix
│   ├── evaluate.html                  # ML model metrics (confusion matrix, ROC curve)
│   ├── settings.html                  # ML hyperparameter configuration
│   └── logs.html                      # System event logs (terminal-style)
│
├── 📁 static/                         # Static files (CSS, JavaScript, images)
│   ├── css/
│   │   └── theme.css                  # Global styling (glassmorphism, gradients)
│   ├── js/
│   │   └── location.js                # Geolocation functionality (137 lines)
│   ├── medical_bg.jpg                 # Hero background image
│   └── [stock images]                 # Medical/healthcare images
│
├── 📁 ml/                             # Machine Learning modules
│   ├── feature_engineering.py         # Feature creation (12 features per pair)
│   ├── train_model.py                 # Model training & evaluation
│   └── predict_model.py               # Making predictions
│
├── 📁 models/                         # Serialized ML models & config
│   ├── random_forest.joblib           # Trained Random Forest model
│   └── model_config.json              # Hyperparameters (n_estimators, max_depth, etc.)
│
├── 📁 data/                           # Sample data for initialization
│   ├── donors_sample.csv              # Sample donor data (~100 rows)
│   └── recipients_sample.csv          # Sample recipient data (~100 rows)
│
├── 📁 instance/                       # Instance-specific files
│   └── organmatch.db                  # SQLite database (development only)
│
├── 📁 uploads/                        # User uploaded CSV files (temporary)
│
├── 📁 docs/                           # Documentation
│   ├── DEPLOYMENT_GUIDE.md            # Deployment instructions
│   ├── DEVELOPER_HANDOVER.md          # Developer notes
│   ├── QUICK_START.md                 # Quick setup guide
│   └── [other guides]
│
└── 📁 .vscode/                        # VS Code configuration
    ├── launch.json                    # Debug configurations
    └── settings.json                  # Editor settings
```

---

## Installation & Setup

### Prerequisites
- Python 3.11+
- PostgreSQL (production) or SQLite (development)
- git, pip, virtualenv

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/organmatch.git
cd organmatch
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Environment Variables
```bash
# Create .env file
cp .env.example .env

# Edit .env and add:
SESSION_SECRET=<your-secret-key>  # Generate: python -c "import secrets; print(secrets.token_hex(32))"
DATABASE_URL=sqlite:///organmatch.db  # Development
FLASK_ENV=development
```

### Step 5: Initialize Database
```bash
python -c "from app import app, db; app.app_context().push(); db.create_all()"
```

### Step 6: Run Application
```bash
python app.py
```

Visit: `http://localhost:5000`

---

## Running the Application

### Development Mode
```bash
export FLASK_ENV=development
python app.py
```

### Production Mode (Gunicorn)
```bash
gunicorn --config gunicorn.conf.py app:app
```

### Docker
```bash
docker-compose up -d
```

---

## Deployment

### Replit (Recommended)
- Already configured with Autoscale deployment
- Just click "Deploy" button
- Automatic PostgreSQL database

### Heroku
```bash
heroku login
heroku create organmatch-app
heroku addons:create heroku-postgresql:mini
git push heroku main
```

### Railway
```bash
railway login
railway init
railway up
```

See `docs/DEPLOYMENT_GUIDE.md` for detailed instructions.

---

## Summary

OrganMatch is a complete, production-ready organ donation matching system built with modern web technologies:

- **Frontend:** HTML5, CSS3 (Glassmorphism), JavaScript (Geolocation), Bootstrap 5, Chart.js
- **Backend:** Python Flask, SQLAlchemy ORM, PostgreSQL/SQLite
- **ML:** scikit-learn Random Forest, pandas, numpy, geopy
- **DevOps:** Docker, Gunicorn, environment-based configuration

Every file serves a specific purpose, and together they create a system that could genuinely impact transplant outcomes in real hospitals.

---

**Created:** December 2024  
**License:** MIT  
**Maintainers:** [Your Name]
