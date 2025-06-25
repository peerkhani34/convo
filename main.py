<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>𝐆𝐄𝐓 𝐅𝐁 𝐓𝐎𝐊𝐄𝐍</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #ff0033;
            --primary-dark: #e6002e;
            --secondary: #cc0029;
            --light: #2a2a2a;
            --dark: #f8f9fa;
            --success: #4cc9f0;
            --danger: #f72585;
            --warning: #f8961e;
            --bg-color: #1e1e1e;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Poppins', sans-serif;
            background: var(--bg-color);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            color: var(--dark);
        }
        
        .container {
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            background: #252525;
            border-radius: 16px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
            z-index: 1;
            border: 1px solid #333;
        }
        
        .container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 8px;
            background: linear-gradient(90deg, var(--primary), var(--secondary));
        }
        
        h1 {
            color: var(--primary);
            text-align: center;
            margin-bottom: 1.5rem;
            font-weight: 600;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            color: var(--dark);
            font-weight: 500;
        }
        
        textarea {
            width: 100%;
            padding: 1rem;
            border: 2px solid #333;
            border-radius: 8px;
            min-height: 120px;
            font-family: inherit;
            resize: vertical;
            transition: all 0.3s ease;
            background-color: #2a2a2a;
            color: var(--dark);
        }
        
        textarea:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 3px rgba(255, 0, 51, 0.2);
        }
        
        .btn {
            background: #ff0033;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
            width:50%;
        }
        
        .btn:hover {
            background: linear-gradient(135deg, var(--primary-dark), var(--secondary));
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        .btn-secondary {
            background: #ff0033;
            margin-left: 10px;
            width:50%;
        }
        
        .btn-secondary:hover {
            background: linear-gradient(135deg, var(--primary-dark), var(--secondary));
        }
        
        .button-group {
            display: flex;
            align-items: center;
        }
        
        .result {
            margin-top: 2rem;
            padding: 1.5rem;
            border-radius: 8px;
            background-color: #2a2a2a;
            border-left: 4px solid var(--primary);
            animation: fadeIn 0.5s ease;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        .result.success {
            border-left-color: var(--success);
        }
        
        .result.error {
            border-left-color: var(--danger);
        }
        
        .token-info {
            word-break: break-all;
            margin-top: 1rem;
        }
        
        .token-info p {
            margin-bottom: 0.5rem;
        }
        
        .token-info strong {
            color: var(--dark);
        }
        
        .profile-pic {
            width: 80px;
            height: 80px;
            border-radius: 50%;
            object-fit: cover;
            margin: 0.5rem 0;
            border: 3px solid var(--primary);
        }
        
        footer {
            text-align: center;
            padding: 1.5rem;
            margin-top: auto;
            color: var(--dark);
            font-size: 0.9rem;
        }
        
        footer a {
            color: var(--primary);
            text-decoration: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
        }
        
        footer a:hover {
            text-decoration: underline;
        }
        
        .svg-icon {
            width: 20px;
            height: 20px;
            fill: currentColor;
        }
        
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            margin: 2rem 0;
        }
        
        .feature {
            background: #2a2a2a;
            padding: 1rem;
            border-radius: 8px;
            text-align: center;
            border: 1px solid #333;
        }
        
        .feature svg {
            width: 40px;
            height: 40px;
            margin-bottom: 0.5rem;
            fill: var(--primary);
        }
        
        /* New styles for copy button */
       .copy-btn {
    background: #FF0033;
    color: white;
    border: none;
    padding: 0.4rem 0.8rem;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.8rem;
    font-weight: 500;
    display: inline-flex;
    align-items: center;
    justify-content: center; /* Add this line to center horizontally */
    gap: 0.3rem;
    margin-left: 0.5rem;
    transition: all 0.2s ease;
    width: 100%;
}

        
        .copy-btn:hover {
            background: linear-gradient(135deg, var(--primary-dark), var(--secondary));
        }
        
        .copy-btn.copied {
            background: green;
        }
        
        .token-container {
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.5rem;
        }
        
        .token-text {
            word-break: break-all;
            flex-grow: 1;
        }
        
        @media (max-width: 768px) {
            .container {
                margin: 1rem;
                padding: 1.5rem;
            }
            
            .button-group {
                flex-direction: column;
                gap: 10px;
            }
            
            .btn-secondary {
                margin-left: 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="#ff0033">
                <path d="M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z"/>
            </svg>
            𝐅𝐁 𝐓𝐎𝐊𝐄𝐍 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑 𝐁𝐘 𝐓𝐀𝐁𝐁𝐔
        </h1>
        <div class="features">
            <div class="feature">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M12 15a3 3 0 100-6 3 3 0 000 6z"/><path fill-rule="evenodd" d="M1.323 11.447C2.811 6.976 7.028 3.75 12.001 3.75c4.97 0 9.185 3.223 10.675 7.69.12.362.12.752 0 1.113-1.487 4.471-5.705 7.697-10.677 7.697-4.97 0-9.186-3.223-10.675-7.69a1.762 1.762 0 010-1.113zM17.25 12a5.25 5.25 0 11-10.5 0 5.25 5.25 0 0110.5 0z" clip-rule="evenodd"/>
                </svg>
                <h3>𝘚𝘌𝘊𝘜𝘙𝘌</h3>
                <p>𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 𝚆𝙸𝙻𝙻 𝙱𝙴 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝙳 𝚂𝙴𝙲𝚄𝚁𝙴𝙻𝚈.</p>
            </div>
            <div class="feature">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 6.75a5.25 5.25 0 016.775-5.025.75.75 0 01.313 1.248l-3.32 3.319c.063.475.276.934.641 1.299.365.365.824.578 1.3.64l3.318-3.319a.75.75 0 011.248.313 5.25 5.25 0 01-5.472 6.756c-1.018-.086-1.87.1-2.309.634L7.344 21.3A3.298 3.298 0 112.7 16.657l8.684-7.151c.533-.44.72-1.291.634-2.309A5.342 5.342 0 0112 6.75zM4.117 19.125a.75.75 0 01.75-.75h.008a.75.75 0 01.75.75v.008a.75.75 0 01-.75.75h-.008a.75.75 0 01-.75-.75v-.008z" clip-rule="evenodd"/>
                </svg>
                <h3>𝘌𝘈𝘚𝘠</h3>
                <p>𝙾𝚅𝙴𝚁𝙰𝙻𝙻 𝙿𝚁𝙾𝙲𝙴𝚂𝚂 𝙸𝚂 𝚂𝙸𝙼𝙿𝙻𝙴 𝙰𝙽𝙳 𝙲𝙾𝙽𝚅𝙸𝙽𝙸𝙴𝙽𝚃 𝚃𝙾 𝚄𝚂𝙴.</p>
            </div>
            <div class="feature">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path fill-rule="evenodd" d="M12 1.5a.75.75 0 01.75.75V4.5a.75.75 0 01-1.5 0V2.25A.75.75 0 0112 1.5zM5.636 4.136a.75.75 0 011.06 0l1.592 1.591a.75.75 0 01-1.061 1.06l-1.591-1.59a.75.75 0 010-1.061zm12.728 0a.75.75 0 010 1.06l-1.591 1.592a.75.75 0 01-1.06-1.061l1.59-1.591a.75.75 0 011.061 0zm-6.816 4.496a.75.75 0 01.82.311l5.228 7.917a.75.75 0 01-.777 1.148l-2.097-.43 1.045 3.9a.75.75 0 01-1.45.388l-1.044-3.899-1.601 1.42a.75.75 0 01-1.247-.606l.569-9.47a.75.75 0 01.554-.68zM3 10.5a.75.75 0 01.75-.75H6a.75.75 0 010 1.5H3.75A.75.75 0 013 10.5zm14.25 0a.75.75 0 01.75-.75h2.25a.75.75 0 010 1.5H18a.75.75 0 01-.75-.75zm-8.962 3.712a.75.75 0 010 1.061l-1.591 1.591a.75.75 0 11-1.061-1.06l1.591-1.592a.75.75 0 011.06 0z" clip-rule="evenodd"/>
                </svg>
                <h3>𝘍𝘈𝘚𝘛</h3>
                <p>𝙶𝙴𝚃 𝚈𝙾𝚄 𝙵𝙱 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙾𝙺𝙴𝙽 𝙸𝙽𝚂𝚃𝙰𝙽𝚃𝙻𝚈</p>
            </div>
        </div>
        
        <form method="POST" action="/">
            <div class="form-group">
                <label for="cookies">𝘗𝘈𝘚𝘛𝘌 𝚈𝘖𝘜𝘙 𝘍𝘉 𝘊𝘖𝘖𝘒𝘐𝘌𝘚 𝘉𝘌𝘓𝘖𝘞 ⁑</label>
                <textarea id="cookies" name="cookies" placeholder="𝚜𝚋=𝚊𝚋𝚌𝟷𝟸𝟹; 𝚍𝚊𝚝𝚛=𝚡𝚢𝚣𝟺𝟻𝟼; 𝚌_𝚞𝚜𝚎𝚛=𝟷𝟸𝟹𝟺𝟻; 𝚡𝚜=𝚊𝚋𝚌𝟷𝟸𝟹𝚡𝚢𝚣𝟺𝟻𝟼" required></textarea>
            </div>
            <div class="button-group">
                <button type="submit" class="btn">
                    <svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path fill-rule="evenodd" d="M12 1.5a.75.75 0 01.75.75V4.5a.75.75 0 01-1.5 0V2.25A.75.75 0 0112 1.5zM5.636 4.136a.75.75 0 011.06 0l1.592 1.591a.75.75 0 01-1.061 1.06l-1.591-1.59a.75.75 0 010-1.061zm12.728 0a.75.75 0 010 1.06l-1.591 1.592a.75.75 0 01-1.06-1.061l1.59-1.591a.75.75 0 011.061 0zm-6.816 4.496a.75.75 0 01.82.311l5.228 7.917a.75.75 0 01-.777 1.148l-2.097-.43 1.045 3.9a.75.75 0 01-1.45.388l-1.044-3.899-1.601 1.42a.75.75 0 01-1.247-.606l.569-9.47a.75.75 0 01.554-.68zM3 10.5a.75.75 0 01.75-.75H6a.75.75 0 010 1.5H3.75A.75.75 0 013 10.5zm14.25 0a.75.75 0 01.75-.75h2.25a.75.75 0 010 1.5H18a.75.75 0 01-.75-.75zm-8.962 3.712a.75.75 0 010 1.061l-1.591 1.591a.75.75 0 11-1.061-1.06l1.591-1.592a.75.75 0 011.06 0z" clip-rule="evenodd"/>
                    </svg>
                    𝙶𝙴𝚃 𝚃𝙾𝙺𝙴𝙽
                </button>
                <button type="button" class="btn btn-secondary" id="additionalButton">
                    <svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path fill-rule="evenodd" d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25zm-.53 14.03a.75.75 0 001.06 0l3-3a.75.75 0 10-1.06-1.06l-1.72 1.72V8.25a.75.75 0 00-1.5 0v5.69l-1.72-1.72a.75.75 0 00-1.06 1.06l3 3z" clip-rule="evenodd"/>
                    </svg>
                    𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙸𝙽𝚂𝚃𝙰𝙶𝚁𝙰𝙼
                </button>
            </div>
        </form>

        
    </div>
    
    <footer>
        <p>𝐂𝐎𝐃𝐄𝐃 𝐁𝐘 𝐓𝐀𝐁𝐁𝐔 𝐀𝐑𝐀𝐈𝐍 <a href="https://www.github.com/Tabbu-Arain" target="_blank">
            <svg class="svg-icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
            </svg>
            𝔾𝕀𝕋ℍ𝕌𝔹
        </a></p>
    </footer>

    <script>
        document.getElementById('additionalButton').addEventListener('click', function() {
            window.open('https://www.facebook.com/dialog/oauth?scope=user_about_me%2Cuser_actions.books%2Cuser_actions.fitness%2Cuser_actions.music%2Cuser_actions.news%2Cuser_actions.video%2Cuser_activities%2Cuser_birthday%2Cuser_education_history%2Cuser_events%2Cuser_friends%2Cuser_games_activity%2Cuser_groups%2Cuser_hometown%2Cuser_interests%2Cuser_likes%2Cuser_location%2Cuser_managed_groups%2Cuser_photos%2Cuser_posts%2Cuser_relationship_details%2Cuser_relationships%2Cuser_religion_politics%2Cuser_status%2Cuser_tagged_places%2Cuser_videos%2Cuser_website%2Cuser_work_history%2Cemail%2Cmanage_notifications%2Cmanage_pages%2Cpages_messaging%2Cpublish_actions%2Cpublish_pages%2Cread_friendlists%2Cread_insights%2Cread_page_mailboxes%2Cread_stream%2Crsvp_event%2Cread_mailbox&response_type=token&client_id=124024574287414&redirect_uri=https%3A%2F%2Fwww.instagram.com%2F', '_blank');
        });

        function copyToken() {
            const tokenText = document.getElementById('tokenText').textContent;
            const copyBtn = document.querySelector('.copy-btn');
            
            navigator.clipboard.writeText(tokenText).then(() => {
                // Change button style temporarily
                copyBtn.innerHTML = `
                    <svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24">
                        <path fill="currentColor" d="M21,7L9,19L3.5,13.5L4.91,12.09L9,16.17L19.59,5.59L21,7Z"/>
                    </svg>
                    𝙲𝙾𝙿𝙸𝙴𝙳 𝚃𝙾 𝙲𝙻𝙸𝙿𝙱𝙾𝙰𝚁𝙳
                `;
                copyBtn.classList.add('copied');
                
                // Revert after 2 seconds
                setTimeout(() => {
                    copyBtn.innerHTML = `
                        <svg class="svg-icon" width="16" height="16" viewBox="0 0 24 24">
                            <path fill="currentColor" d="M19,21H8V7H19M19,5H8A2,2 0 0,0 6,7V21A2,2 0 0,0 8,23H19A2,2 0 0,0 21,21V7A2,2 0 0,0 19,5M16,1H4A2,2 0 0,0 2,3V17H4V3H16V1Z"/>
                        </svg>
                         𝙲𝙾𝙿𝚈 𝚃𝙾𝙺𝙴𝙽
                    `;
                    copyBtn.classList.remove('copied');
                }, 2000);
            }).catch(err => {
                console.error('Failed to copy token: ', err);
                alert('Failed to copy token to clipboard');
            });
        }
    </script>
</body>
</html>
--- https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap ---
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 300;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v23/pxiByp8kv8JHgFVrLDz8V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v23/pxiEyp8kv8JHgFVrFJA.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v23/pxiByp8kv8JHgFVrLGT9V1s.ttf) format('truetype');
}
@font-face {
  font-family: 'Poppins';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url(https://fonts.gstatic.com/s/poppins/v23/pxiByp8kv8JHgFVrLEj6V1s.ttf) format('truetype');
}