document.addEventListener('DOMContentLoaded', function() {
    // 1. Intercept Subscribe Forms (Newsletter)
    const subscribeForms = document.querySelectorAll('.subscribe-form');
    subscribeForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            submitToMailchimp(form, 'newsletter');
        });
    });

    // 2. Intercept Waitlist Forms (Modals and Contact Page)
    const waitlistForms = document.querySelectorAll('.waitlist-form');
    waitlistForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            submitToMailchimp(form, 'waitlist');
        });
    });
});

function submitToMailchimp(form, type) {
    // Change UI to loading state
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.innerHTML : '';
    if (submitBtn) {
        submitBtn.innerHTML = 'Enviando...';
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.7';
    }

    const url = form.action.replace('/post?', '/post-json?');
    const formData = new FormData(form);
    const params = new URLSearchParams(formData);
    
    // Create a unique callback name
    const callbackName = 'mcCallback_' + Math.round(100000 * Math.random());
    window[callbackName] = function(data) {
        delete window[callbackName];
        const scriptTags = document.querySelectorAll(`script[src*="${callbackName}"]`);
        scriptTags.forEach(tag => tag.remove());
        
        if (data.result === 'error') {
            if (submitBtn) {
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
                submitBtn.style.opacity = '1';
            }
            // Clean up mailchimp HTML errors
            let cleanMsg = data.msg.replace(/(<([^>]+)>)/gi, "");
            alert("Error: " + cleanMsg);
            return;
        }
        
        handleSuccess(form, type);
    };
    
    params.append('c', callbackName);
    
    // Append script to DOM to trigger JSONP
    const script = document.createElement('script');
    script.src = url + '&' + params.toString();
    document.body.appendChild(script);
}

function handleSuccess(form, type) {
    const isSpanish = window.location.pathname.includes('_es') || document.documentElement.lang === 'es';
    
    // If it's a contact form (check SOURCE hidden input)
    const sourceInput = form.querySelector('input[name="SOURCE"]');
    const sourceValue = sourceInput ? sourceInput.value : '';
    
    if (sourceValue === 'Contacto' || sourceValue === 'Contact') {
        window.location.href = isSpanish ? 'gracias.html' : 'thank-you.html';
        return;
    }
    
    if (type === 'newsletter') {
        // Inline success for footer/hero
        form.innerHTML = `
            <div style="background: #F5E8F6; color: #A03FA3; padding: 16px 24px; border-radius: 6px; font-weight: 500; display: flex; flex-direction: column; align-items: center; gap: 12px; width: 100%; justify-content: center;">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                    <span>${isSpanish ? '¡Gracias por suscribirte!' : 'Thanks for subscribing!'}</span>
                </div>
                <a href="${isSpanish ? 'masterclass_es.html' : 'masterclass.html'}" style="background-color: #A03FA3; color: white; padding: 8px 24px; border-radius: 50px; text-decoration: none; font-size: 13px; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; transition: opacity 0.2s;">
                    ${isSpanish ? 'Únete a nuestra Masterclass' : 'Join our Masterclass'}
                </a>
            </div>
        `;
    } else if (type === 'waitlist') {
        // Modal success: Replace the top title and description texts directly
        const modalContainer = form.parentElement;
        if (modalContainer) {
            const title = modalContainer.querySelector('h2');
            const desc = modalContainer.querySelector('p');
            
            if (title) {
                title.innerText = isSpanish ? 'Ya estás dentro.' : "You're in.";
            }
            if (desc) {
                desc.innerText = isSpanish ? 'El sistema operativo de tu riqueza está en construcción.' : 'The operating system for your wealth is being built.';
            }
        }

        form.innerHTML = `
            <div style="text-align: center; padding: 20px 0;">
                <div style="width: 80px; height: 80px; background-color: #F5E8F6; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 24px;">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#A03FA3" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
                        <polyline points="20 6 9 17 4 12"></polyline>
                    </svg>
                </div>
                <p style="font-size: 1.1rem; color: #666; margin-bottom: 24px; line-height: 1.5;">${isSpanish ? 'Pronto recibirás todo lo que necesitas para empezar a construir tu castillo, directo a tu correo.' : "You'll soon receive everything you need to start building your castle, straight to your inbox."}</p>
            </div>
        `;
    }
}
