import re

file_path = "/Users/Naty/.gemini/antigravity/scratch/castle-update/masterclass_v2.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_sections = """
    <!-- 1. Hero Section -->
    <style>
        /* Force white header on this page */
        #main-header { background: rgba(255, 255, 255, 0.98) !important; backdrop-filter: blur(12px) !important; border-bottom: 1px solid #E5E7EB !important; padding: 16px clamp(30px, 5vw, 100px) !important; }
        #main-header .logo-light { display: none !important; }
        #main-header .logo-dark { display: block !important; }
        #main-header .nav-links a { color: #1A1A1A !important; }
        #main-header .nav-links a:hover { color: #A03FA3 !important; }
        #main-header .lang-select { color: #1A1A1A !important; border-color: #E5E7EB !important; background-image: url('data:image/svg+xml;utf8,<svg fill="%231A1A1A" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg"><path d="M7 10l5 5 5-5z"/><path d="M0 0h24v24H0z" fill="none"/></svg>') !important; }
        .mobile-menu-toggle { color: #1A1A1A !important; }
    </style>
    <section class="hero snap-section" style="background: url('./public/images/common/masterclass-hero.png?v=1') center/cover no-repeat; display: flex; align-items: flex-end; padding: 150px 4vw 40px 4vw; min-height: 100vh; position: relative;">
        <!-- Black Gradient Overlay -->
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%); z-index: 1;"></div>
        
        <div class="container" style="max-width: 1000px; margin: 0 auto; display: flex; justify-content: center; align-items: center; position: relative; z-index: 2;">
            <div style="text-align: center; width: 100%;">
                <div style="color: #A03FA3; font-weight: 700; font-size: clamp(20px, 3vw, 24px); letter-spacing: 4px; margin-bottom: 20px;">Castle MasterClass Series</div>
                <h1 class="hero-title" style="color: #FFFFFF; font-size: clamp(24px, 5vw, 84px); white-space: nowrap; line-height: 1.1; letter-spacing: -2px; margin-bottom: var(--spacer-30); text-shadow: 0 4px 12px rgba(0,0,0,0.5);">
                    Money Reset for Women™
                </h1>
                <p style="color: rgba(255,255,255,0.95); font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; margin-bottom: 0; font-weight: 500;">
                    A 4-Day Immersive Experience to Rewire Wealth,<br>Build Confidence & Make Money Work for You.
                </p>

            </div>
        </div>
    </section>

    <!-- 2. Subhero / Bajada -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 50px 4vw; border-bottom: 1px solid #F3F4F6;">
        <div class="color-reveal" style="width: 100%; max-width: 1400px; margin: 0 auto; text-align: center;">
            <h2 class="section-heading color-reveal" style="margin-bottom: 30px; font-size: clamp(38px, 6vw, 75px); line-height: 1.1; letter-spacing: -2px; font-weight: 500; color: #1A1A1A;">
                This is not another financial literacy class.
            </h2>
            <div class="color-reveal section-subtitle" style="margin-bottom: 30px;">
                <p class="section-subtitle-1" style="font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; color: #86868B; font-weight: 500; margin: 0;">This is a transformational masterclass experience designed to help women:</p>
            </div>
            
            <div class="mobile-scroll-row" id="subhero-scroll" style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px; text-align: left;">
                
                <!-- Box 1 -->
                <div style="aspect-ratio: 2/3; position: relative; border-radius: 5px; overflow: hidden; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%), url('./public/images/common/step1.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: flex-end; padding: 25px 15px; transition: transform 0.3s;">
                    <div style="position: relative; z-index: 2; text-align: center;">
                        <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(28px, 2.5vw, 36px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 6px;">Break</span>
                        <span style="display: flex; align-items: flex-start; justify-content: center; min-height: 2.8em; font-family: 'Inter', sans-serif; font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">limiting money beliefs</span>
                    </div>
                </div>

                <!-- Box 2 -->
                <div style="aspect-ratio: 2/3; position: relative; border-radius: 5px; overflow: hidden; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%), url('./public/images/common/step2.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: flex-end; padding: 25px 15px; transition: transform 0.3s;">
                    <div style="position: relative; z-index: 2; text-align: center;">
                        <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(28px, 2.5vw, 36px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 6px;">Overcome</span>
                        <span style="display: flex; align-items: flex-start; justify-content: center; min-height: 2.8em; font-family: 'Inter', sans-serif; font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">fear & imposter syndrome</span>
                    </div>
                </div>

                <!-- Box 3 -->
                <div style="aspect-ratio: 2/3; position: relative; border-radius: 5px; overflow: hidden; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%), url('./public/images/common/step3.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: flex-end; padding: 25px 15px; transition: transform 0.3s;">
                    <div style="position: relative; z-index: 2; text-align: center;">
                        <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(28px, 2.5vw, 36px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 6px;">Understand</span>
                        <span style="display: flex; align-items: flex-start; justify-content: center; min-height: 2.8em; font-family: 'Inter', sans-serif; font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">your financial reality</span>
                    </div>
                </div>

                <!-- Box 4 -->
                <div style="aspect-ratio: 2/3; position: relative; border-radius: 5px; overflow: hidden; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%), url('./public/images/common/step4.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: flex-end; padding: 25px 15px; transition: transform 0.3s;">
                    <div style="position: relative; z-index: 2; text-align: center;">
                        <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(28px, 2.5vw, 36px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 6px;">Rewire</span>
                        <span style="display: flex; align-items: flex-start; justify-content: center; min-height: 2.8em; font-family: 'Inter', sans-serif; font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">your relationship with money</span>
                    </div>
                </div>

                <!-- Box 5 -->
                <div style="aspect-ratio: 2/3; position: relative; border-radius: 5px; overflow: hidden; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%), url('./public/images/common/step5.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: flex-end; padding: 25px 15px; transition: transform 0.3s;">
                    <div style="position: relative; z-index: 2; text-align: center;">
                        <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(28px, 2.5vw, 36px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 6px;">Develop</span>
                        <span style="display: flex; align-items: flex-start; justify-content: center; min-height: 2.8em; font-family: 'Inter', sans-serif; font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">investor confidence</span>
                    </div>
                </div>

                <!-- Box 6 -->
                <div style="aspect-ratio: 2/3; position: relative; border-radius: 5px; overflow: hidden; background: linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.85) 100%), url('./public/images/common/buildcastle.jpg') center/cover no-repeat; display: flex; flex-direction: column; justify-content: flex-end; padding: 25px 15px; transition: transform 0.3s;">
                    <div style="position: relative; z-index: 2; text-align: center;">
                        <span style="display: block; font-family: 'Caveat', cursive; font-size: clamp(28px, 2.5vw, 36px); color: #FFFFFF; font-weight: 700; line-height: 1; margin-bottom: 6px;">Create</span>
                        <span style="display: flex; align-items: flex-start; justify-content: center; min-height: 2.8em; font-family: 'Inter', sans-serif; font-size: clamp(12px, 1.1vw, 14px); color: #FFFFFF; font-weight: 400; line-height: 1.3;">a roadmap for wealth</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 3. Program Positioning -->
    <section class="snap-section" style="background-color: #F8F8FA; padding: 50px 4vw; border-bottom: 1px solid #E5E7EB;">
        <div class="color-reveal" style="width: 100%; max-width: 1000px; margin: 0 auto; text-align: center;">
            <h2 class="section-heading color-reveal" style="margin-bottom: 30px; font-size: clamp(38px, 6vw, 75px); line-height: 1.1; letter-spacing: -2px; font-weight: 500; color: #1A1A1A;">
                The program combines:
            </h2>
            
            <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 16px; margin-bottom: 30px;">
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Psychology</div>
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Neuroscience</div>
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Behavioral finance</div>
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Wealth education</div>
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Nervous system regulation</div>
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Strategic financial planning</div>
                <div style="border: 1px solid #A03FA3; background: #FFFFFF; color: #A03FA3; padding: 14px 28px; border-radius: 50px; font-weight: 600; font-size: clamp(16px, 1.5vw, 18px); font-family: 'Inter', sans-serif; display: inline-flex; align-items: center; box-shadow: 0 4px 10px rgba(160,63,163,0.05); transition: transform 0.2s; cursor: default;">Mindset transformation</div>
            </div>

            <div class="color-reveal section-subtitle">
                <p class="section-subtitle-1" style="font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; color: #86868B; font-weight: 500;">
                    The objective is not only to teach women about money.
                </p>
                <p class="section-subtitle-2" style="font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; color: #1A1A1A; font-weight: 600;">
                    The objective is to help them become women who confidently manage, grow, and multiply wealth.
                </p>
            </div>
        </div>
    </section>

    <!-- 4. Core Promise / Full Image -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 50px 4vw; border-bottom: 1px solid #E5E7EB;">
        <div class="container color-reveal" style="display: flex; align-items: center; justify-content: center; min-height: 400px; max-width: 1400px; margin: 0 auto; text-align: center;">
            <div style="width: 100%;">
                <h2 style="font-size: clamp(24px, 4vw, 42px); line-height: 1.15; letter-spacing: -0.02em; font-weight: 500; color: #1A1A1A; font-family: 'Inter', sans-serif;">
                    <span style="display: block; font-family: 'Caveat', cursive; font-weight: 700; color: #A03FA3; font-size: clamp(42px, 6vw, 75px); letter-spacing: 0; margin-bottom: 5px;">In Four Transformative Days,</span>
                    women will uncover the hidden beliefs limiting their financial growth, rewire their relationship with money, understand their financial reality clearly, and develop the confidence and strategy to begin building long-term wealth.
                </h2>
            </div>
        </div>
    </section>

    <!-- 5. Who This Is For -->
    <section class="snap-section" style="background: url('./public/images/common/who-this-is-for-bg.png') center/cover no-repeat; position: relative; padding: 100px 4vw; border-bottom: 1px solid #E5E7EB;">
        <div style="position: absolute; inset: 0; background: linear-gradient(180deg, rgba(0,0,0,0.3) 0%, rgba(0,0,0,0.7) 100%); z-index: 1;"></div>
        <div class="container" style="position: relative; z-index: 2; max-width: 1200px; margin: 0 auto; text-align: center;">
            <h2 class="section-heading" style="margin-bottom: 30px; font-size: clamp(38px, 6vw, 75px); line-height: 1.1; letter-spacing: -2px; font-weight: 500; color: #FFFFFF; text-shadow: 0 4px 20px rgba(0,0,0,0.4);">
                Who This Is For
            </h2>
            <p class="section-subtitle-1" style="font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; color: rgba(255,255,255,0.9); font-weight: 500; margin-bottom: 40px; text-shadow: 0 2px 10px rgba(0,0,0,0.3);">
                Women who:
            </p>
            
            <div style="max-width: 900px; margin: 0 auto; background: rgba(255, 255, 255, 0.1); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255, 255, 255, 0.2); border-radius: 30px; padding: 40px 50px; font-size: clamp(18px, 2vw, 24px); line-height: 1.8; color: #FFFFFF; font-weight: 400; text-align: left; box-shadow: 0 10px 40px rgba(0,0,0,0.2);">
                Want financial independence. Earn money but do not feel financially empowered. Feel overwhelmed by investing or financial planning. Struggle with confidence around money. Want to transition from survival to ownership. Are entrepreneurs, professionals, executives, creators, or founders. Want to make smarter financial decisions. 
                <span style="display: block; margin-top: 20px; font-weight: 700; color: #F3D2F5; font-size: 1.1em;">Want to create wealth intentionally.</span>
            </div>
        </div>
    </section>


    <!-- 7. The 4-Day Journey -->
    <section class="snap-section" style="background-color: #FFFFFF; padding: 50px 4vw; border-bottom: 1px solid #F3F4F6;">
        <div class="container" style="max-width: 1400px; margin: 0 auto;">
            <div style="text-align: center; margin-bottom: 30px;">
                <h2 class="section-heading" style="margin-bottom: 30px; font-size: clamp(38px, 6vw, 75px); line-height: 1.1; letter-spacing: -2px; font-weight: 500; color: #1A1A1A;">
                    The 4-Day Masterclass Structure
                </h2>
            </div>
            
            <style>
            .masterclass-flip-card {
                background-color: transparent;
                perspective: 1000px;
                min-height: 480px;
                height: 100%;
            }
            .masterclass-flip-card-inner {
                position: relative;
                width: 100%;
                height: 100%;
                text-align: left;
                transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
                transform-style: preserve-3d;
                cursor: pointer;
            }
            .masterclass-flip-card:hover .masterclass-flip-card-inner {
                transform: rotateY(180deg);
            }
            .masterclass-flip-card-front, .masterclass-flip-card-back {
                position: absolute;
                width: 100%;
                height: 100%;
                -webkit-backface-visibility: hidden;
                backface-visibility: hidden;
                border-radius: 5px;
            }
            .masterclass-flip-card-front {
                display: flex;
                flex-direction: column;
                justify-content: flex-end;
                padding: 40px 30px;
                background-size: cover !important;
                background-position: center !important;
                border: 1px solid #E5E7EB;
            }
            .masterclass-flip-card-front::after {
                content: "";
                position: absolute;
                inset: 0;
                background: linear-gradient(to top, rgba(0,0,0,0.95) 0%, rgba(0,0,0,0) 60%);
                border-radius: 5px;
                z-index: 1;
            }
            .masterclass-flip-card-front > div {
                position: relative;
                z-index: 2;
            }
            .masterclass-flip-card-back {
                background-color: #F8F8FA;
                border: 1px solid #E5E7EB;
                padding: 60px 24px 30px;
                transform: rotateY(180deg);
                display: flex;
                flex-direction: column;
                overflow-y: auto;
            }
            .masterclass-flip-card-back h4 {
                text-transform: capitalize;
            }
            .masterclass-flip-card-back ul li {
                margin-bottom: 24px !important;
            }
            </style>

            <div id="journey-scroll" class="mobile-scroll-row" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
                
                <!-- Day 1 -->
                <div class="masterclass-flip-card">
                    <div class="masterclass-flip-card-inner">
                        <div class="masterclass-flip-card-front" style="background: url('./public/images/common/step1.jpg')">
                            <div>
                                <div style="color: #F8F8FA; font-weight: 800; font-size: 16px; letter-spacing: 2px; margin-bottom: 12px; font-family: 'Inter', sans-serif;">DAY 1</div>
                                <h3 style="font-size: 28px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px; font-family: 'Inter', sans-serif;">Breaking the Money Wall</h3>
                                <p style="font-size: 15px; font-weight: 400; color: #E5E7EB; margin-bottom: 0; font-family: 'Inter', sans-serif;">"Understanding the Hidden Programming"</p>
                            </div>
                        </div>
                        <div class="masterclass-flip-card-back">
                            <div style="flex-grow: 1;">
                                <h4 style="font-size: 20px; color: #1A1A1A; margin-top: 0; margin-bottom: 16px; font-family: 'Inter', sans-serif; font-weight: 700; line-height: 1.4; text-align: center;">
                                    Women cannot transform what they cannot see.
                                </h4>
                                <ul style="list-style: none; padding: 0; margin-bottom: 20px;">
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Uncover limiting beliefs & inherited patterns
                                    </li>
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Address imposter syndrome & emotional conditioning
                                    </li>
                                </ul>
                            </div>
                            
                            <div style="background: rgba(160,63,163,0.08); padding: 20px; border-radius: 5px;">
                                <p style="font-size: 16px; color: #1A1A1A; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif; text-align: center;">Awareness of what has been unconsciously limiting you</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Day 2 -->
                <div class="masterclass-flip-card">
                    <div class="masterclass-flip-card-inner">
                        <div class="masterclass-flip-card-front" style="background: url('./public/images/common/step2.jpg')">
                            <div>
                                <div style="color: #F8F8FA; font-weight: 800; font-size: 16px; letter-spacing: 2px; margin-bottom: 12px; font-family: 'Inter', sans-serif;">DAY 2</div>
                                <h3 style="font-size: 28px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px; font-family: 'Inter', sans-serif;">Neuro-Wealth Rewiring</h3>
                                <p style="font-size: 15px; font-weight: 400; color: #E5E7EB; margin-bottom: 0; font-family: 'Inter', sans-serif;">"Reprogramming the Financial Mind"</p>
                            </div>
                        </div>
                        <div class="masterclass-flip-card-back">
                            <div style="flex-grow: 1;">
                                <h4 style="font-size: 20px; color: #1A1A1A; margin-top: 0; margin-bottom: 16px; font-family: 'Inter', sans-serif; font-weight: 700; line-height: 1.4; text-align: center;">
                                    The brain and nervous system can be retrained.
                                </h4>
                                <ul style="list-style: none; padding: 0; margin-bottom: 20px;">
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Harness neuroplasticity & emotional regulation
                                    </li>
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Rewire reactions to fear, success, and visibility
                                    </li>
                                </ul>
                            </div>
                            
                            <div style="background: rgba(160,63,163,0.08); padding: 20px; border-radius: 5px;">
                                <p style="font-size: 16px; color: #1A1A1A; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif; text-align: center;">Beginning to feel safer with wealth and visibility</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Day 3 -->
                <div class="masterclass-flip-card">
                    <div class="masterclass-flip-card-inner">
                        <div class="masterclass-flip-card-front" style="background: url('./public/images/common/step3.jpg')">
                            <div>
                                <div style="color: #F8F8FA; font-weight: 800; font-size: 16px; letter-spacing: 2px; margin-bottom: 12px; font-family: 'Inter', sans-serif;">DAY 3</div>
                                <h3 style="font-size: 28px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px; font-family: 'Inter', sans-serif;">Financial Reality Reset</h3>
                                <p style="font-size: 15px; font-weight: 400; color: #E5E7EB; margin-bottom: 0; font-family: 'Inter', sans-serif;">"Understanding Your Money Clearly"</p>
                            </div>
                        </div>
                        <div class="masterclass-flip-card-back">
                            <div style="flex-grow: 1;">
                                <h4 style="font-size: 20px; color: #1A1A1A; margin-top: 0; margin-bottom: 16px; font-family: 'Inter', sans-serif; font-weight: 700; line-height: 1.4; text-align: center;">
                                    Empowerment requires absolute clarity.
                                </h4>
                                <ul style="list-style: none; padding: 0; margin-bottom: 20px;">
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Build financial self-awareness without fear
                                    </li>
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Create a personal dashboard & wealth vision
                                    </li>
                                </ul>
                            </div>
                            
                            <div style="background: rgba(160,63,163,0.08); padding: 20px; border-radius: 5px;">
                                <p style="font-size: 16px; color: #1A1A1A; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif; text-align: center;">Clarity, control, and practical financial awareness</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Day 4 -->
                <div class="masterclass-flip-card">
                    <div class="masterclass-flip-card-inner">
                        <div class="masterclass-flip-card-front" style="background: url('./public/images/common/step4.jpg')">
                            <div>
                                <div style="color: #F8F8FA; font-weight: 800; font-size: 16px; letter-spacing: 2px; margin-bottom: 12px; font-family: 'Inter', sans-serif;">DAY 4</div>
                                <h3 style="font-size: 28px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px; font-family: 'Inter', sans-serif;">Building the Future</h3>
                                <p style="font-size: 15px; font-weight: 400; color: #E5E7EB; margin-bottom: 0; font-family: 'Inter', sans-serif;">"Making Money Work for You"</p>
                            </div>
                        </div>
                        <div class="masterclass-flip-card-back">
                            <div style="flex-grow: 1;">
                                <h4 style="font-size: 20px; color: #1A1A1A; margin-top: 0; margin-bottom: 16px; font-family: 'Inter', sans-serif; font-weight: 700; line-height: 1.4; text-align: center;">
                                    Wealth is built strategically.
                                </h4>
                                <ul style="list-style: none; padding: 0; margin-bottom: 20px;">
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Learn the fundamentals of investing & risk
                                    </li>
                                    <li style="font-size: 15px; color: #2A2A2A; margin-bottom: 16px; position: relative; padding-left: 20px; font-family: 'Inter', sans-serif; font-weight: 500;">
                                        <span style="position: absolute; left: 0; top: 7px; width: 6px; height: 6px; border-radius: 50%; background-color: #1A1A1A;"></span>Design a personalized, long-term wealth roadmap
                                    </li>
                                </ul>
                            </div>
                            
                            <div style="background: rgba(160,63,163,0.08); padding: 20px; border-radius: 5px;">
                                <p style="font-size: 16px; color: #1A1A1A; font-weight: 700; margin: 0; font-family: 'Inter', sans-serif; text-align: center;">A clear action plan and strategy to build wealth</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
            <div class="mobile-scroll-indicators" data-target="journey-scroll"></div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="javascript:void(0);" onclick="openUnifiedModal('waitlist');" class="btn" style="background-color: #A03FA3; border: none; color: #FFFFFF; font-weight: 800; padding: 18px 45px; border-radius: 50px; display: inline-block; text-transform: uppercase; letter-spacing: 1px; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">
                    Apply for the Masterclass
                </a>
            </div>
        </div>
    </section>


    <!-- 9. What Makes This Different -->
    <section class="snap-section" style="background: url('./public/images/common/final-cta-bg.png') center/cover no-repeat; position: relative; min-height: 100vh; display: flex; align-items: flex-end; justify-content: center; padding: 50px 4vw 80px 4vw; text-align: center;">
        <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(0,0,0,0.9) 100%); z-index: 1;"></div>
        
        <div class="container" style="position: relative; z-index: 2; width: 100%; max-width: 1200px; margin: 0 auto; display: flex; flex-direction: column; align-items: center;">
            <h2 style="width: 100%; margin-bottom: 30px; font-size: clamp(38px, 6vw, 75px); line-height: 1.1; letter-spacing: -2px; font-weight: 700; color: #FFFFFF; font-family: 'Inter', sans-serif;">
                What Makes This Different
            </h2>
            <p style="font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; color: rgba(255,255,255,0.9); font-weight: 500; margin-bottom: 30px; font-family: 'Inter', sans-serif;">
                Unlike traditional financial education, this program addresses:
            </p>
            
            <div class="pill-scroll-row" style="display: flex; flex-wrap: nowrap; overflow-x: auto; justify-content: center; gap: 12px; margin-bottom: 40px; width: 100%; align-items: center; align-content: center; max-width: 1300px; padding-bottom: 10px;">
                <span style="padding: 14px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.4); background: rgba(255,255,255,0.05); backdrop-filter: blur(8px); color: #FFFFFF; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 15px; white-space: nowrap; text-transform: capitalize;">psychology</span>
                <span style="padding: 14px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.4); background: rgba(255,255,255,0.05); backdrop-filter: blur(8px); color: #FFFFFF; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 15px; white-space: nowrap; text-transform: capitalize;">identity</span>
                <span style="padding: 14px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.4); background: rgba(255,255,255,0.05); backdrop-filter: blur(8px); color: #FFFFFF; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 15px; white-space: nowrap; text-transform: capitalize;">emotional patterns</span>
                <span style="padding: 14px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.4); background: rgba(255,255,255,0.05); backdrop-filter: blur(8px); color: #FFFFFF; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 15px; white-space: nowrap; text-transform: capitalize;">nervous system conditioning</span>
                <span style="padding: 14px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.4); background: rgba(255,255,255,0.05); backdrop-filter: blur(8px); color: #FFFFFF; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 15px; white-space: nowrap; text-transform: capitalize;">confidence</span>
                <span style="padding: 14px 24px; border-radius: 50px; border: 1px solid rgba(255,255,255,0.4); background: rgba(255,255,255,0.05); backdrop-filter: blur(8px); color: #FFFFFF; font-weight: 700; font-family: 'Inter', sans-serif; font-size: 15px; white-space: nowrap; text-transform: capitalize;">behavioral change</span>
            </div>

            <p style="font-size: clamp(18px, 2.5vw, 24px); line-height: 1.6; color: rgba(255,255,255,0.9); font-weight: 500; margin-bottom: 30px; font-family: 'Inter', sans-serif;">
                Not just: budgets and investing. <strong style="color: #FFFFFF;">This creates a deeper transformation.</strong>
            </p>
            
            <a href="javascript:void(0);" onclick="openUnifiedModal('waitlist');" class="btn" style="background-color: #A03FA3 !important; border: none; color: #FFFFFF !important; font-weight: 800; padding: 18px 45px; border-radius: 50px; display: inline-block; text-transform: uppercase; letter-spacing: 1px; transition: transform 0.3s;" onmouseover="this.style.transform='scale(1.05)';" onmouseout="this.style.transform='scale(1)';">
                APPLY NOW
            </a>
        </div>
    </section>

"""

# Everything up to </header>
headerSplitPoint = "</header>"
footerSplitPoint = '<footer class="site-footer">'

if headerSplitPoint in content and footerSplitPoint in content:
    top_part = content.split(headerSplitPoint)[0] + headerSplitPoint
    bottom_part = footerSplitPoint + content.split(footerSplitPoint)[1]
    
    final_content = top_part + "\n\n" + new_sections + "\n\n    " + bottom_part
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(final_content)
        
    print("Replaced all sections successfully.")
else:
    print("Could not find split points")
