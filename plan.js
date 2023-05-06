//
// [회원가입]
// ========================================

// 1. id 중복검사 :
// POST users/id/existence
const request1 = { userId: '...' };
const response1 = { result: true };

// 2. random unique nickname generator :
// GET users/nickname
const response2 = { nickname: '...' };

// 3. 회원가입
// POST users/sign-up
const request3 = { userId: '...', nickname: '...', password: '...' };
const response3 = { result: true };

// 4. 로그인
// GET auths/token
const response4 = { accessToken: '...', refreshToken: '...' };

// 5. refreshToken 으로 accessToken 갱신
// POST auths/refresh
const request5 = { refreshToken: '...' };
const response5 = { accessToken: '...', refreshToken: '...' };
2;
