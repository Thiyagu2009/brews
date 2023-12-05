
<h1>Brewsy Email Analytics Dashboard</h1>

<h3>Overview</h3>

<p><strong>Application Link:</strong> <a href="https://brewsey.streamlit.app">Brewsy Email Analytics Dashboard</a></p>

<p>This application collects user email addresses and interests to send personalized email content. Email addresses and trigger counts are stored in the Supabase database and dynamically displayed in a DataFrame. Email views are tracked, and corresponding statistics for the last 90 days are updated every minute.</p>

<p><strong>Note:</strong> Check spam folders for received emails.</p>

<h4>Technologies Used</h4>

<ul>
    <li><strong>Streamlit:</strong> Used for creating the interactive dashboard.</li>
    <li><strong>Supabase:</strong> Utilized for database storage and retrieval.</li>
    <li><strong>Brevo:</strong> Integrated for email functionality and analytics.</li>
    <li><strong>ChatGPT:</strong> Planned for generating personalized email content based on user interests (code is currently commented out due to a lack of tokens).</li>
</ul>

<h3>Usage</h3>

<ol>
    <li>Access the <a href="https://brewsey.streamlit.app">Brewsy Email Analytics Dashboard</a>.</li>
    <li>Provide your email address and interests to receive personalized email content.</li>
    <li>View email analytics, including trigger counts and view statistics over the last 90 days.</li>
    <li>Check spam folders for received emails.</li>
</ol>

<h3>Implementation Details</h3>

<h4>Streamlit Dashboard</h4>

<p>The interactive dashboard is built using Streamlit, providing a user-friendly interface for collecting user data and displaying email analytics.</p>

<h4>Supabase Database</h4>

<p>Supabase is used as the backend database to store user email addresses, trigger counts, and view statistics.</p>

<h4>Brevo Email Integration & Analytics</h4>

<p>Brevo is integrated to facilitate email functionality, and analytics are used to track email views and display corresponding statistics.</p>

<h4>ChatGPT (Code Commented Out)</h4>

<p>The application plans to use ChatGPT for generating personalized email content based on user interests. However, the code is currently commented out due to a lack of API tokens.</p>

<h3>Notes</h3>

<ul>
    <li>The dashboard includes a link to the application for user convenience.</li>
    <li>Email view statistics are refreshed every minute.</li>
    <li>Check spam folders for received emails to ensure content visibility.</li>
</ul>

<p>Feel free to customize and expand upon the provided README based on your specific project requirements and details.</p>

