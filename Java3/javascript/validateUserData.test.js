// validateUserData.test.js
const validateUserData = require('./validateUserData');

test('valid user data', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25,
        referralCode: 'ABCDEFGH'
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(true);
});

test('invalid email format', () => {
    const userData = {
        username: 'validUser123',
        email: 'invalidemail.com',
        password: 'password1!',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.email).toBe('Invalid email format');
});

test('password too short', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'short',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.password).toBe('Password must be at least 8 characters long');
});

test('password without number', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password!',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.password).toBe('Password must contain at least one number');
});

test('password without special character', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password123',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.password).toBe('Password must contain at least one special character');
});

test('username too short', () => {
    const userData = {
        username: 'ab',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.username).toBe('Username must be between 3 and 20 characters');
});

test('username too long', () => {
    const userData = {
        username: 'thisUsernameIsWayTooLongForOurRequirements123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.username).toBe('Username must be between 3 and 20 characters');
});

test('username with special characters', () => {
    const userData = {
        username: 'invalid#user',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.username).toBe('Username can only contain letters, numbers, and underscores');
});

test('age under 18', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 17
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.age).toBe('User must be at least 18 years old');
});

test('age is not a number', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 'twenty-five'
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.age).toBe('Age must be a number');
});

test('missing referral code', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(true); // Referral code is optional
});

test('referral code too short', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25,
        referralCode: 'ABC'
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.referralCode).toBe('Referral code must be exactly 8 characters');
});

test('referral code too long', () => {
    const userData = {
        username: 'validUser123',
        email: 'validuser@example.com',
        password: 'password1!',
        age: 25,
        referralCode: 'ABCDEFGHIJKLM'
    };
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.referralCode).toBe('Referral code must be exactly 8 characters');
});

test('invalid global user data', () => {
    const userData = 'stringInsteadOfObject';
    const result = validateUserData(userData);
    expect(result.isValid).toBe(false);
    expect(result.errors.global).toBe('Invalid user data format');
});
