// validateUserData.js

function validateUserData(userData) {
    const result = {
        isValid: true,
        errors: {}
    };

    // Check if userData exists and is an object
    if (!userData || typeof userData !== 'object') {
        result.isValid = false;
        result.errors.global = "Invalid user data format";
        return result;
    }

    // Validate username
    if (!userData.username) {
        result.isValid = false;
        result.errors.username = "Username is required";
    } else if (userData.username.length < 3 || userData.username.length > 20) {
        result.isValid = false;
        result.errors.username = "Username must be between 3 and 20 characters";
    } else if (!/^[a-zA-Z0-9_]+$/.test(userData.username)) {
        result.isValid = false;
        result.errors.username = "Username can only contain letters, numbers, and underscores";
    }

    // Validate email
    if (!userData.email) {
        result.isValid = false;
        result.errors.email = "Email is required";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userData.email)) {
        result.isValid = false;
        result.errors.email = "Invalid email format";
    }

    // Validate password
    if (!userData.password) {
        result.isValid = false;
        result.errors.password = "Password is required";
    } else if (userData.password.length < 8) {
        result.isValid = false;
        result.errors.password = "Password must be at least 8 characters long";
    } else if (!/\d/.test(userData.password)) {
        result.isValid = false;
        result.errors.password = "Password must contain at least one number";
    } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(userData.password)) {
        result.isValid = false;
        result.errors.password = "Password must contain at least one special character";
    }

    // Validate age (optional)
    if (userData.age !== undefined) {
        if (typeof userData.age !== 'number') {
            result.isValid = false;
            result.errors.age = "Age must be a number";
        } else if (userData.age < 18) {
            result.isValid = false;
            result.errors.age = "User must be at least 18 years old";
        }
    }

    // Validate referral code (optional)
    if (userData.referralCode !== undefined) {
        if (typeof userData.referralCode !== 'string') {
            result.isValid = false;
            result.errors.referralCode = "Referral code must be a string";
        } else if (userData.referralCode.length !== 8) {
            result.isValid = false;
            result.errors.referralCode = "Referral code must be exactly 8 characters";
        }
    }

    return result;
}

module.exports = validateUserData;
