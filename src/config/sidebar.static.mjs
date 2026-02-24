export const staticSidebar = [
{
	label: 'Codex',
	translations: { en: 'Codex' },
	items: [
		{ slug: 'codex', label: 'Codex', translations: { en: 'Codex' } },
		// Getting Started
		{
			label: '시작하기',
			translations: { en: 'Getting Started' },
			items: [
				{ slug: 'codex/overview', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'codex/quickstart', label: '빠른 시작', translations: { en: 'Quickstart' } },
				{ slug: 'codex/explore', label: '탐색', translations: { en: 'Explore' } },
				{ slug: 'codex/pricing', label: '가격', translations: { en: 'Pricing' } },
				{
					label: '개념',
					translations: { en: 'Concepts' },
					items: [
						{ slug: 'codex/prompting', label: '프롬프팅', translations: { en: 'Prompting' } },
						{ slug: 'codex/concepts/customization', label: '맞춤화', translations: { en: 'Customization' } },
						{ slug: 'codex/concepts/multi-agents', label: '멀티 에이전트', translations: { en: 'Multi-agents' } },
						{ slug: 'codex/workflows', label: '워크플로', translations: { en: 'Workflows' } },
						{ slug: 'codex/models', label: '모델', translations: { en: 'Models' } },
						{ slug: 'codex/concepts/cyber-safety', label: '사이버 안전', translations: { en: 'Cyber Safety' } },
					],
				},
			],
		},
		// Using Codex
		{
			label: 'Codex 사용하기',
			translations: { en: 'Using Codex' },
			items: [
				{
					label: '앱',
					translations: { en: 'App' },
					items: [
						{ slug: 'codex/app', label: '개요', translations: { en: 'Overview' } },
						{ slug: 'codex/app/features', label: '기능', translations: { en: 'Features' } },
						{ slug: 'codex/app/settings', label: '설정', translations: { en: 'Settings' } },
						{ slug: 'codex/app/review', label: '리뷰', translations: { en: 'Review' } },
						{ slug: 'codex/app/automations', label: '자동화', translations: { en: 'Automations' } },
						{ slug: 'codex/app/worktrees', label: '워크트리', translations: { en: 'Worktrees' } },
						{ slug: 'codex/app/local-environments', label: '로컬 환경', translations: { en: 'Local Environments' } },
						{ slug: 'codex/app/commands', label: '명령어', translations: { en: 'Commands' } },
						{ slug: 'codex/app/troubleshooting', label: '문제 해결', translations: { en: 'Troubleshooting' } },
					],
				},
				{
					label: 'IDE 확장',
					translations: { en: 'IDE Extension' },
					items: [
						{ slug: 'codex/ide', label: '개요', translations: { en: 'Overview' } },
						{ slug: 'codex/ide/features', label: '기능', translations: { en: 'Features' } },
						{ slug: 'codex/ide/settings', label: '설정', translations: { en: 'Settings' } },
						{ slug: 'codex/ide/commands', label: 'IDE 명령어', translations: { en: 'IDE Commands' } },
						{ slug: 'codex/ide/slash-commands', label: '슬래시 명령어', translations: { en: 'Slash commands' } },
					],
				},
				{
					label: 'CLI',
					items: [
						{ slug: 'codex/cli', label: '개요', translations: { en: 'Overview' } },
						{ slug: 'codex/cli/features', label: '기능', translations: { en: 'Features' } },
						{ slug: 'codex/cli/reference', label: '명령줄 옵션', translations: { en: 'Command Line Options' } },
						{ slug: 'codex/cli/slash-commands', label: '슬래시 명령어', translations: { en: 'Slash commands' } },
					],
				},
				{
					label: '웹',
					translations: { en: 'Web' },
					items: [
						{ slug: 'codex/cloud', label: '개요', translations: { en: 'Overview' } },
						{ slug: 'codex/cloud/environments', label: '환경', translations: { en: 'Environments' } },
						{ slug: 'codex/cloud/internet-access', label: '인터넷 액세스', translations: { en: 'Internet Access' } },
					],
				},
				{
					label: '통합',
					translations: { en: 'Integrations' },
					items: [
						{ slug: 'codex/integrations/github', label: 'GitHub', translations: { en: 'GitHub' } },
						{ slug: 'codex/integrations/slack', label: 'Slack', translations: { en: 'Slack' } },
						{ slug: 'codex/integrations/linear', label: 'Linear', translations: { en: 'Linear' } },
					],
				},
			],
		},
		// Configuration
		{
			label: '설정',
			translations: { en: 'Configuration' },
			items: [
				{ slug: 'codex/config-basic', label: 'Config 기본', translations: { en: 'Config Basics' } },
				{ slug: 'codex/config-advanced', label: '고급 Config', translations: { en: 'Advanced Config' } },
				{ slug: 'codex/config-reference', label: 'Config 레퍼런스', translations: { en: 'Config Reference' } },
				{ slug: 'codex/config-sample', label: 'Config 샘플', translations: { en: 'Sample Config' } },
				{ slug: 'codex/rules', label: '규칙', translations: { en: 'Rules' } },
				{ slug: 'codex/guides/agents-md', label: 'AGENTS.md', translations: { en: 'AGENTS.md' } },
				{ slug: 'codex/mcp', label: 'MCP', translations: { en: 'MCP' } },
				{ slug: 'codex/skills', label: '스킬', translations: { en: 'Skills' } },
				{ slug: 'codex/custom-prompts', label: '커스텀 프롬프트', translations: { en: 'Custom Prompts' } },
				{ slug: 'codex/multi-agent', label: '멀티 에이전트', translations: { en: 'Multi-agents' } },
			],
		},
		// Administration
		{
			label: '관리',
			translations: { en: 'Administration' },
			items: [
				{ slug: 'codex/auth', label: '인증', translations: { en: 'Authentication' } },
				{ slug: 'codex/security', label: '보안', translations: { en: 'Security' } },
				{
					label: '엔터프라이즈',
					translations: { en: 'Enterprise' },
					items: [
						{ slug: 'codex/enterprise/admin-setup', label: '관리자 설정', translations: { en: 'Admin Setup' } },
						{ slug: 'codex/enterprise/governance', label: '거버넌스', translations: { en: 'Governance' } },
					],
				},
				{ slug: 'codex/windows', label: 'Windows', translations: { en: 'Windows' } },
			],
		},
		// Automation
		{
			label: '자동화',
			translations: { en: 'Automation' },
			items: [
				{ slug: 'codex/noninteractive', label: '비대화형 모드', translations: { en: 'Non-interactive Mode' } },
				{ slug: 'codex/sdk', label: 'Codex SDK', translations: { en: 'Codex SDK' } },
				{ slug: 'codex/app-server', label: '앱 서버', translations: { en: 'App Server' } },
				{ slug: 'codex/github-action', label: 'GitHub Action', translations: { en: 'GitHub Action' } },
			],
		},
		// Learn
		{
			label: '학습',
			translations: { en: 'Learn' },
			items: [
				{ slug: 'codex/videos', label: '영상', translations: { en: 'Videos' } },
				{ slug: 'codex/guides/agents-sdk', label: 'Agents SDK', translations: { en: 'Agents SDK' } },
				{ slug: 'codex/guides/build-ai-native-engineering-team', label: 'AI 네이티브 팀 구성', translations: { en: 'Building AI Teams' } },
			],
		},
		// Community
		{
			label: '커뮤니티',
			translations: { en: 'Community' },
			items: [
				{ slug: 'codex/ambassadors', label: '앰배서더', translations: { en: 'Ambassadors' } },
				{ slug: 'codex/community/meetups', label: '밋업', translations: { en: 'Meetups' } },
			],
		},
		// Releases
		{
			label: '릴리스',
			translations: { en: 'Releases' },
			items: [
				{ slug: 'codex/changelog', label: '변경 로그', translations: { en: 'Changelog' } },
				{ slug: 'codex/feature-maturity', label: '기능 성숙도', translations: { en: 'Feature Maturity' } },
				{ slug: 'codex/open-source', label: '오픈 소스', translations: { en: 'Open Source' } },
			],
		},
	],
},
	{
label: 'Next.js',
translations: { en: 'Next.js' },
items: [
	{ slug: 'nextjs', label: 'Next.js', translations: { en: 'Next.js' } },
	{
		label: 'App Router',
		translations: { en: 'App Router' },
		items: [
		{
			label: '시작하기',
			translations: { en: 'Getting Started' },
			items: [
			{ slug: 'nextjs/app/getting-started', label: '개요', translations: { en: 'Overview' } },
			{ slug: 'nextjs/app/getting-started/installation', label: '설치', translations: { en: 'Installation' } },
			{ slug: 'nextjs/app/getting-started/project-structure', label: '프로젝트 구조', translations: { en: 'Project Structure' } },
			{ slug: 'nextjs/app/getting-started/layouts-and-pages', label: '레이아웃과 페이지', translations: { en: 'Layouts and Pages' } },
			{ slug: 'nextjs/app/getting-started/linking-and-navigating', label: '링크 및 탐색', translations: { en: 'Linking and Navigating' } },
			{ slug: 'nextjs/app/getting-started/server-and-client-components', label: '서버와 클라이언트 컴포넌트', translations: { en: 'Server and Client Components' } },
			{ slug: 'nextjs/app/getting-started/cache-components', label: '컴포넌트 캐시', translations: { en: 'Cache Components' } },
			{ slug: 'nextjs/app/getting-started/fetching-data', label: '데이터 가져오기', translations: { en: 'Fetching Data' } },
			{ slug: 'nextjs/app/getting-started/updating-data', label: '데이터 업데이트', translations: { en: 'Updating Data' } },
			{ slug: 'nextjs/app/getting-started/caching-and-revalidating', label: '캐싱과 재검증', translations: { en: 'Caching and Revalidating' } },
			{ slug: 'nextjs/app/getting-started/error-handling', label: '오류 처리', translations: { en: 'Error Handling' } },
			{ slug: 'nextjs/app/getting-started/css', label: 'CSS', translations: { en: 'CSS' } },
			{ slug: 'nextjs/app/getting-started/images', label: '이미지 최적화', translations: { en: 'Image Optimization' } },
			{ slug: 'nextjs/app/getting-started/fonts', label: '폰트 최적화', translations: { en: 'Font Optimization' } },
			{ slug: 'nextjs/app/getting-started/metadata-and-og-images', label: '메타데이터와 OG 이미지', translations: { en: 'Metadata and OG images' } },
			{ slug: 'nextjs/app/getting-started/route-handlers', label: '라우트 핸들러', translations: { en: 'Route Handlers' } },
			{ slug: 'nextjs/app/getting-started/proxy', label: '프록시', translations: { en: 'Proxy' } },
			{ slug: 'nextjs/app/getting-started/deploying', label: '배포', translations: { en: 'Deploying' } },
			{ slug: 'nextjs/app/getting-started/upgrading', label: '업그레이드', translations: { en: 'Upgrading' } }
			],
		},
		{
			label: '가이드',
			translations: { en: 'Guides' },
			items: [
			{ slug: 'nextjs/app/guides', label: '개요', translations: { en: 'Overview' } },
			{ slug: 'nextjs/app/guides/ai-agents', label: 'AI 코딩 에이전트', translations: { en: 'AI Coding Agents' } },
			{ slug: 'nextjs/app/guides/analytics', label: '분석', translations: { en: 'Analytics' } },
			{ slug: 'nextjs/app/guides/authentication', label: '인증', translations: { en: 'Authentication' } },
			{ slug: 'nextjs/app/guides/backend-for-frontend', label: '백엔드 포 프론트엔드', translations: { en: 'Backend for Frontend' } },
			{ slug: 'nextjs/app/guides/caching', label: '캐싱', translations: { en: 'Caching' } },
			{ slug: 'nextjs/app/guides/ci-build-caching', label: 'CI 빌드 캐싱', translations: { en: 'CI Build Caching' } },
			{ slug: 'nextjs/app/guides/content-security-policy', label: '콘텐츠 보안 정책', translations: { en: 'Content Security Policy' } },
			{ slug: 'nextjs/app/guides/css-in-js', label: 'CSS-in-JS', translations: { en: 'CSS-in-JS' } },
			{ slug: 'nextjs/app/guides/custom-server', label: '커스텀 서버', translations: { en: 'Custom Server' } },
			{ slug: 'nextjs/app/guides/data-security', label: '데이터 보안', translations: { en: 'Data Security' } },
			{ slug: 'nextjs/app/guides/debugging', label: '디버깅', translations: { en: 'Debugging' } },
			{ slug: 'nextjs/app/guides/draft-mode', label: '드래프트 모드', translations: { en: 'Draft Mode' } },
			{ slug: 'nextjs/app/guides/environment-variables', label: '환경 변수', translations: { en: 'Environment Variables' } },
			{ slug: 'nextjs/app/guides/forms', label: '폼', translations: { en: 'Forms' } },
			{ slug: 'nextjs/app/guides/incremental-static-regeneration', label: 'ISR', translations: { en: 'ISR' } },
			{ slug: 'nextjs/app/guides/instrumentation', label: '계측', translations: { en: 'Instrumentation' } },
			{ slug: 'nextjs/app/guides/internationalization', label: '국제화', translations: { en: 'Internationalization' } },
			{ slug: 'nextjs/app/guides/json-ld', label: 'JSON-LD', translations: { en: 'JSON-LD' } },
			{ slug: 'nextjs/app/guides/lazy-loading', label: '지연 로딩', translations: { en: 'Lazy Loading' } },
			{ slug: 'nextjs/app/guides/local-development', label: '개발 환경', translations: { en: 'Development Environment' } },
			{ slug: 'nextjs/app/guides/mcp', label: 'Next.js MCP 서버', translations: { en: 'Next.js MCP Server' } },
			{ slug: 'nextjs/app/guides/mdx', label: 'MDX', translations: { en: 'MDX' } },
			{ slug: 'nextjs/app/guides/memory-usage', label: '메모리 사용', translations: { en: 'Memory Usage' } },
			{
				label: '마이그레이션',
				translations: { en: 'Migrating' },
				items: [
				{ slug: 'nextjs/app/guides/migrating', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/guides/migrating/app-router-migration', label: 'App Router', translations: { en: 'App Router' } },
				{ slug: 'nextjs/app/guides/migrating/from-create-react-app', label: 'Create React App', translations: { en: 'Create React App' } },
				{ slug: 'nextjs/app/guides/migrating/from-vite', label: 'Vite', translations: { en: 'Vite' } }
				],
			},
			{ slug: 'nextjs/app/guides/multi-tenant', label: '멀티 테넌트', translations: { en: 'Multi-tenant' } },
			{ slug: 'nextjs/app/guides/multi-zones', label: '멀티 존', translations: { en: 'Multi-zones' } },
			{ slug: 'nextjs/app/guides/open-telemetry', label: 'OpenTelemetry', translations: { en: 'OpenTelemetry' } },
			{ slug: 'nextjs/app/guides/package-bundling', label: '패키지 번들링', translations: { en: 'Package Bundling' } },
			{ slug: 'nextjs/app/guides/prefetching', label: '프리페칭', translations: { en: 'Prefetching' } },
			{ slug: 'nextjs/app/guides/production-checklist', label: '프로덕션', translations: { en: 'Production' } },
			{ slug: 'nextjs/app/guides/progressive-web-apps', label: 'PWA', translations: { en: 'PWAs' } },
			{ slug: 'nextjs/app/guides/public-static-pages', label: '공개 페이지', translations: { en: 'Public pages' } },
			{ slug: 'nextjs/app/guides/redirecting', label: '리다이렉트', translations: { en: 'Redirecting' } },
			{ slug: 'nextjs/app/guides/sass', label: 'Sass', translations: { en: 'Sass' } },
			{ slug: 'nextjs/app/guides/scripts', label: '스크립트', translations: { en: 'Scripts' } },
			{ slug: 'nextjs/app/guides/self-hosting', label: '셀프 호스팅', translations: { en: 'Self-Hosting' } },
			{ slug: 'nextjs/app/guides/single-page-applications', label: 'SPA', translations: { en: 'SPAs' } },
			{ slug: 'nextjs/app/guides/static-exports', label: '정적 내보내기', translations: { en: 'Static Exports' } },
			{ slug: 'nextjs/app/guides/tailwind-v3-css', label: 'Tailwind CSS v3', translations: { en: 'Tailwind CSS v3' } },
			{
				label: '테스팅',
				translations: { en: 'Testing' },
				items: [
				{ slug: 'nextjs/app/guides/testing', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/guides/testing/cypress', label: 'Cypress', translations: { en: 'Cypress' } },
				{ slug: 'nextjs/app/guides/testing/jest', label: 'Jest', translations: { en: 'Jest' } },
				{ slug: 'nextjs/app/guides/testing/playwright', label: 'Playwright', translations: { en: 'Playwright' } },
				{ slug: 'nextjs/app/guides/testing/vitest', label: 'Vitest', translations: { en: 'Vitest' } }
				],
			},
			{ slug: 'nextjs/app/guides/third-party-libraries', label: '서드파티 라이브러리', translations: { en: 'Third Party Libraries' } },
			{
				label: '업그레이드',
				translations: { en: 'Upgrading' },
				items: [
				{ slug: 'nextjs/app/guides/upgrading', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/guides/upgrading/codemods', label: 'Codemods', translations: { en: 'Codemods' } },
				{ slug: 'nextjs/app/guides/upgrading/version-14', label: '버전 14', translations: { en: 'Version 14' } },
				{ slug: 'nextjs/app/guides/upgrading/version-15', label: '버전 15', translations: { en: 'Version 15' } },
				{ slug: 'nextjs/app/guides/upgrading/version-16', label: '버전 16', translations: { en: 'Version 16' } }
				],
			},
			{ slug: 'nextjs/app/guides/videos', label: '동영상', translations: { en: 'Videos' } }
			],
		},
		{
			label: 'API 참조',
			translations: { en: 'API Reference' },
			items: [
			{ slug: 'nextjs/app/api-reference', label: '개요', translations: { en: 'Overview' } },
			{
				label: '지시어',
				translations: { en: 'Directives' },
				items: [
				{ slug: 'nextjs/app/api-reference/directives', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/api-reference/directives/use-cache', label: 'use cache', translations: { en: 'use cache' } },
				{ slug: 'nextjs/app/api-reference/directives/use-cache-private', label: 'use cache: private', translations: { en: 'use cache: private' } },
				{ slug: 'nextjs/app/api-reference/directives/use-cache-remote', label: 'use cache: remote', translations: { en: 'use cache: remote' } },
				{ slug: 'nextjs/app/api-reference/directives/use-client', label: 'use client', translations: { en: 'use client' } },
				{ slug: 'nextjs/app/api-reference/directives/use-server', label: 'use server', translations: { en: 'use server' } }
				],
			},
			{
				label: '컴포넌트',
				translations: { en: 'Components' },
				items: [
				{ slug: 'nextjs/app/api-reference/components', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/api-reference/components/font', label: '폰트', translations: { en: 'Font' } },
				{ slug: 'nextjs/app/api-reference/components/form', label: '폼 컴포넌트', translations: { en: 'Form Component' } },
				{ slug: 'nextjs/app/api-reference/components/image', label: '이미지 컴포넌트', translations: { en: 'Image Component' } },
				{ slug: 'nextjs/app/api-reference/components/link', label: '링크 컴포넌트', translations: { en: 'Link Component' } },
				{ slug: 'nextjs/app/api-reference/components/script', label: '스크립트 컴포넌트', translations: { en: 'Script Component' } }
				],
			},
			{
				label: '파일 시스템 컨벤션',
				translations: { en: 'File-system conventions' },
				items: [
				{ slug: 'nextjs/app/api-reference/file-conventions', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/default', label: 'default.js', translations: { en: 'default.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/dynamic-routes', label: '동적 세그먼트', translations: { en: 'Dynamic Segments' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/error', label: 'error.js', translations: { en: 'error.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/forbidden', label: 'forbidden.js', translations: { en: 'forbidden.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/instrumentation', label: 'instrumentation.js', translations: { en: 'instrumentation.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/instrumentation-client', label: 'instrumentation-client.js', translations: { en: 'instrumentation-client.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/intercepting-routes', label: '인터셉팅 라우트', translations: { en: 'Intercepting Routes' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/layout', label: 'layout.js', translations: { en: 'layout.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/loading', label: 'loading.js', translations: { en: 'loading.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/mdx-components', label: 'mdx-components.js', translations: { en: 'mdx-components.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/not-found', label: 'not-found.js', translations: { en: 'not-found.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/page', label: 'page.js', translations: { en: 'page.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/parallel-routes', label: '병렬 라우트', translations: { en: 'Parallel Routes' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/proxy', label: 'proxy.js', translations: { en: 'proxy.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/public-folder', label: 'public', translations: { en: 'public' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/route', label: 'route.js', translations: { en: 'route.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/route-groups', label: '라우트 그룹', translations: { en: 'Route Groups' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/route-segment-config', label: '라우트 세그먼트 구성', translations: { en: 'Route Segment Config' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/src-folder', label: 'src', translations: { en: 'src' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/template', label: 'template.js', translations: { en: 'template.js' } },
				{ slug: 'nextjs/app/api-reference/file-conventions/unauthorized', label: 'unauthorized.js', translations: { en: 'unauthorized.js' } },
				{
					label: '메타데이터 파일',
					translations: { en: 'Metadata Files' },
					items: [
					{ slug: 'nextjs/app/api-reference/file-conventions/metadata', label: '개요', translations: { en: 'Overview' } },
					{ slug: 'nextjs/app/api-reference/file-conventions/metadata/app-icons', label: 'favicon, icon, and apple-icon', translations: { en: 'favicon, icon, and apple-icon' } },
					{ slug: 'nextjs/app/api-reference/file-conventions/metadata/manifest', label: 'manifest.json', translations: { en: 'manifest.json' } },
					{ slug: 'nextjs/app/api-reference/file-conventions/metadata/opengraph-image', label: 'opengraph-image and twitter-image', translations: { en: 'opengraph-image and twitter-image' } },
					{ slug: 'nextjs/app/api-reference/file-conventions/metadata/robots', label: 'robots.txt', translations: { en: 'robots.txt' } },
					{ slug: 'nextjs/app/api-reference/file-conventions/metadata/sitemap', label: 'sitemap.xml', translations: { en: 'sitemap.xml' } }
					],
				}
				],
			},
			{
				label: '함수',
				translations: { en: 'Functions' },
				items: [
				{ slug: 'nextjs/app/api-reference/functions', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/api-reference/functions/after', label: 'after', translations: { en: 'after' } },
				{ slug: 'nextjs/app/api-reference/functions/cacheLife', label: 'cacheLife', translations: { en: 'cacheLife' } },
				{ slug: 'nextjs/app/api-reference/functions/cacheTag', label: 'cacheTag', translations: { en: 'cacheTag' } },
				{ slug: 'nextjs/app/api-reference/functions/connection', label: 'connection', translations: { en: 'connection' } },
				{ slug: 'nextjs/app/api-reference/functions/cookies', label: 'cookies', translations: { en: 'cookies' } },
				{ slug: 'nextjs/app/api-reference/functions/draft-mode', label: 'draftMode', translations: { en: 'draftMode' } },
				{ slug: 'nextjs/app/api-reference/functions/fetch', label: 'fetch', translations: { en: 'fetch' } },
				{ slug: 'nextjs/app/api-reference/functions/forbidden', label: 'forbidden', translations: { en: 'forbidden' } },
				{ slug: 'nextjs/app/api-reference/functions/generate-image-metadata', label: 'generateImageMetadata', translations: { en: 'generateImageMetadata' } },
				{ slug: 'nextjs/app/api-reference/functions/generate-metadata', label: 'generateMetadata', translations: { en: 'generateMetadata' } },
				{ slug: 'nextjs/app/api-reference/functions/generate-sitemaps', label: 'generateSitemaps', translations: { en: 'generateSitemaps' } },
				{ slug: 'nextjs/app/api-reference/functions/generate-static-params', label: 'generateStaticParams', translations: { en: 'generateStaticParams' } },
				{ slug: 'nextjs/app/api-reference/functions/generate-viewport', label: 'generateViewport', translations: { en: 'generateViewport' } },
				{ slug: 'nextjs/app/api-reference/functions/headers', label: 'headers', translations: { en: 'headers' } },
				{ slug: 'nextjs/app/api-reference/functions/image-response', label: 'ImageResponse', translations: { en: 'ImageResponse' } },
				{ slug: 'nextjs/app/api-reference/functions/next-request', label: 'NextRequest', translations: { en: 'NextRequest' } },
				{ slug: 'nextjs/app/api-reference/functions/next-response', label: 'NextResponse', translations: { en: 'NextResponse' } },
				{ slug: 'nextjs/app/api-reference/functions/not-found', label: 'notFound', translations: { en: 'notFound' } },
				{ slug: 'nextjs/app/api-reference/functions/permanentRedirect', label: 'permanentRedirect', translations: { en: 'permanentRedirect' } },
				{ slug: 'nextjs/app/api-reference/functions/redirect', label: 'redirect', translations: { en: 'redirect' } },
				{ slug: 'nextjs/app/api-reference/functions/refresh', label: 'refresh', translations: { en: 'refresh' } },
				{ slug: 'nextjs/app/api-reference/functions/revalidatePath', label: 'revalidatePath', translations: { en: 'revalidatePath' } },
				{ slug: 'nextjs/app/api-reference/functions/revalidateTag', label: 'revalidateTag', translations: { en: 'revalidateTag' } },
				{ slug: 'nextjs/app/api-reference/functions/unauthorized', label: 'unauthorized', translations: { en: 'unauthorized' } },
				{ slug: 'nextjs/app/api-reference/functions/unstable_cache', label: 'unstable_cache', translations: { en: 'unstable_cache' } },
				{ slug: 'nextjs/app/api-reference/functions/unstable_noStore', label: 'unstable_noStore', translations: { en: 'unstable_noStore' } },
				{ slug: 'nextjs/app/api-reference/functions/unstable_rethrow', label: 'unstable_rethrow', translations: { en: 'unstable_rethrow' } },
				{ slug: 'nextjs/app/api-reference/functions/updateTag', label: 'updateTag', translations: { en: 'updateTag' } },
				{ slug: 'nextjs/app/api-reference/functions/use-link-status', label: 'useLinkStatus', translations: { en: 'useLinkStatus' } },
				{ slug: 'nextjs/app/api-reference/functions/use-params', label: 'useParams', translations: { en: 'useParams' } },
				{ slug: 'nextjs/app/api-reference/functions/use-pathname', label: 'usePathname', translations: { en: 'usePathname' } },
				{ slug: 'nextjs/app/api-reference/functions/use-report-web-vitals', label: 'useReportWebVitals', translations: { en: 'useReportWebVitals' } },
				{ slug: 'nextjs/app/api-reference/functions/use-router', label: 'useRouter', translations: { en: 'useRouter' } },
				{ slug: 'nextjs/app/api-reference/functions/use-search-params', label: 'useSearchParams', translations: { en: 'useSearchParams' } },
				{ slug: 'nextjs/app/api-reference/functions/use-selected-layout-segment', label: 'useSelectedLayoutSegment', translations: { en: 'useSelectedLayoutSegment' } },
				{ slug: 'nextjs/app/api-reference/functions/use-selected-layout-segments', label: 'useSelectedLayoutSegments', translations: { en: 'useSelectedLayoutSegments' } },
				{ slug: 'nextjs/app/api-reference/functions/userAgent', label: 'userAgent', translations: { en: 'userAgent' } }
				],
			},
			{
				label: '구성',
				translations: { en: 'Configuration' },
				items: [
				{ slug: 'nextjs/app/api-reference/config', label: '개요', translations: { en: 'Overview' } },
				{
					label: 'next.config.js',
					translations: { en: 'next.config.js' },
					items: [
					{ slug: 'nextjs/app/api-reference/config/next-config-js', label: '개요', translations: { en: 'Overview' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/adapterPath', label: 'experimental.adapterPath', translations: { en: 'experimental.adapterPath' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/allowedDevOrigins', label: 'allowedDevOrigins', translations: { en: 'allowedDevOrigins' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/appDir', label: 'appDir', translations: { en: 'appDir' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/assetPrefix', label: 'assetPrefix', translations: { en: 'assetPrefix' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/authInterrupts', label: 'authInterrupts', translations: { en: 'authInterrupts' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/basePath', label: 'basePath', translations: { en: 'basePath' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/browserDebugInfoInTerminal', label: 'browserDebugInfoInTerminal', translations: { en: 'browserDebugInfoInTerminal' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/cacheComponents', label: 'cacheComponents', translations: { en: 'cacheComponents' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/cacheHandlers', label: 'cacheHandlers', translations: { en: 'cacheHandlers' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/cacheLife', label: 'cacheLife', translations: { en: 'cacheLife' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/compress', label: 'compress', translations: { en: 'compress' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/crossOrigin', label: 'crossOrigin', translations: { en: 'crossOrigin' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/cssChunking', label: 'cssChunking', translations: { en: 'cssChunking' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/deploymentId', label: 'deploymentId', translations: { en: 'deploymentId' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/devIndicators', label: 'devIndicators', translations: { en: 'devIndicators' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/distDir', label: 'distDir', translations: { en: 'distDir' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/env', label: 'env', translations: { en: 'env' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/expireTime', label: 'expireTime', translations: { en: 'expireTime' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/exportPathMap', label: 'exportPathMap', translations: { en: 'exportPathMap' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/generateBuildId', label: 'generateBuildId', translations: { en: 'generateBuildId' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/generateEtags', label: 'generateEtags', translations: { en: 'generateEtags' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/headers', label: 'headers', translations: { en: 'headers' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/htmlLimitedBots', label: 'htmlLimitedBots', translations: { en: 'htmlLimitedBots' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/httpAgentOptions', label: 'httpAgentOptions', translations: { en: 'httpAgentOptions' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/images', label: 'images', translations: { en: 'images' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/incrementalCacheHandlerPath', label: 'cacheHandler', translations: { en: 'cacheHandler' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/inlineCss', label: 'inlineCss', translations: { en: 'inlineCss' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/isolatedDevBuild', label: 'isolatedDevBuild', translations: { en: 'isolatedDevBuild' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/logging', label: 'logging', translations: { en: 'logging' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/mdxRs', label: 'mdxRs', translations: { en: 'mdxRs' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/onDemandEntries', label: 'onDemandEntries', translations: { en: 'onDemandEntries' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/optimizePackageImports', label: 'optimizePackageImports', translations: { en: 'optimizePackageImports' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/output', label: 'output', translations: { en: 'output' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/pageExtensions', label: 'pageExtensions', translations: { en: 'pageExtensions' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/poweredByHeader', label: 'poweredByHeader', translations: { en: 'poweredByHeader' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/productionBrowserSourceMaps', label: 'productionBrowserSourceMaps', translations: { en: 'productionBrowserSourceMaps' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/proxyClientMaxBodySize', label: 'proxyClientMaxBodySize', translations: { en: 'proxyClientMaxBodySize' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/reactCompiler', label: 'reactCompiler', translations: { en: 'reactCompiler' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/reactMaxHeadersLength', label: 'reactMaxHeadersLength', translations: { en: 'reactMaxHeadersLength' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/reactStrictMode', label: 'reactStrictMode', translations: { en: 'reactStrictMode' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/redirects', label: 'redirects', translations: { en: 'redirects' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/rewrites', label: 'rewrites', translations: { en: 'rewrites' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/sassOptions', label: 'sassOptions', translations: { en: 'sassOptions' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/serverActions', label: 'serverActions', translations: { en: 'serverActions' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/serverComponentsHmrCache', label: 'serverComponentsHmrCache', translations: { en: 'serverComponentsHmrCache' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/serverExternalPackages', label: 'serverExternalPackages', translations: { en: 'serverExternalPackages' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/staleTimes', label: 'staleTimes', translations: { en: 'staleTimes' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/staticGeneration', label: 'staticGeneration*', translations: { en: 'staticGeneration*' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/taint', label: 'taint', translations: { en: 'taint' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/trailingSlash', label: 'trailingSlash', translations: { en: 'trailingSlash' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/transpilePackages', label: 'transpilePackages', translations: { en: 'transpilePackages' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/turbopack', label: 'turbopack', translations: { en: 'turbopack' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/turbopackFileSystemCache', label: 'turbopackFileSystemCache', translations: { en: 'turbopackFileSystemCache' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/typedRoutes', label: 'typedRoutes', translations: { en: 'typedRoutes' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/typescript', label: 'typescript', translations: { en: 'typescript' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/urlImports', label: 'urlImports', translations: { en: 'urlImports' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/useLightningcss', label: 'useLightningcss', translations: { en: 'useLightningcss' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/viewTransition', label: 'viewTransition', translations: { en: 'viewTransition' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/webpack', label: 'webpack', translations: { en: 'webpack' } },
					{ slug: 'nextjs/app/api-reference/config/next-config-js/webVitalsAttribution', label: 'webVitalsAttribution', translations: { en: 'webVitalsAttribution' } }
					],
				},
				{ slug: 'nextjs/app/api-reference/config/typescript', label: 'TypeScript', translations: { en: 'TypeScript' } },
				{ slug: 'nextjs/app/api-reference/config/eslint', label: 'ESLint', translations: { en: 'ESLint' } }
				],
			},
			{
				label: 'CLI',
				translations: { en: 'CLI' },
				items: [
				{ slug: 'nextjs/app/api-reference/cli', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/app/api-reference/cli/create-next-app', label: 'create-next-app', translations: { en: 'create-next-app' } },
				{ slug: 'nextjs/app/api-reference/cli/next', label: 'next CLI', translations: { en: 'next CLI' } }
				],
			},
			{ slug: 'nextjs/app/api-reference/edge', label: 'Edge Runtime', translations: { en: 'Edge Runtime' } },
			{ slug: 'nextjs/app/api-reference/turbopack', label: 'Turbopack', translations: { en: 'Turbopack' } }
			],
		},
		{ slug: 'nextjs/app/glossary', label: '용어집', translations: { en: 'Glossary' } }
	],
	},
	{
		label: 'Pages Router',
		translations: { en: 'Pages Router' },
		items: [
		{
			label: '시작하기',
			translations: { en: 'Getting Started' },
			items: [
			{ slug: 'nextjs/pages/getting-started', label: '개요', translations: { en: 'Overview' } },
			{ slug: 'nextjs/pages/getting-started/installation', label: '설치', translations: { en: 'Installation' } },
			{ slug: 'nextjs/pages/getting-started/project-structure', label: '프로젝트 구조', translations: { en: 'Project Structure' } },
			{ slug: 'nextjs/pages/getting-started/images', label: 'Images', translations: { en: 'Images' } },
			{ slug: 'nextjs/pages/getting-started/fonts', label: 'Fonts', translations: { en: 'Fonts' } },
			{ slug: 'nextjs/pages/getting-started/css', label: 'CSS', translations: { en: 'CSS' } },
			{ slug: 'nextjs/pages/getting-started/deploying', label: '배포', translations: { en: 'Deploying' } }
			],
		},
		{
			label: '가이드',
			translations: { en: 'Guides' },
			items: [
			{ slug: 'nextjs/pages/guides', label: '개요', translations: { en: 'Overview' } },
			{ slug: 'nextjs/pages/guides/analytics', label: '분석', translations: { en: 'Analytics' } },
			{ slug: 'nextjs/pages/guides/authentication', label: '인증', translations: { en: 'Authentication' } },
			{ slug: 'nextjs/pages/guides/babel', label: 'Babel', translations: { en: 'Babel' } },
			{ slug: 'nextjs/pages/guides/ci-build-caching', label: 'CI 빌드 캐싱', translations: { en: 'CI Build Caching' } },
			{ slug: 'nextjs/pages/guides/content-security-policy', label: '콘텐츠 보안 정책', translations: { en: 'Content Security Policy' } },
			{ slug: 'nextjs/pages/guides/css-in-js', label: 'CSS-in-JS', translations: { en: 'CSS-in-JS' } },
			{ slug: 'nextjs/pages/guides/custom-server', label: '커스텀 서버', translations: { en: 'Custom Server' } },
			{ slug: 'nextjs/pages/guides/debugging', label: '디버깅', translations: { en: 'Debugging' } },
			{ slug: 'nextjs/pages/guides/draft-mode', label: '드래프트 모드', translations: { en: 'Draft Mode' } },
			{ slug: 'nextjs/pages/guides/environment-variables', label: '환경 변수', translations: { en: 'Environment Variables' } },
			{ slug: 'nextjs/pages/guides/forms', label: '폼', translations: { en: 'Forms' } },
			{ slug: 'nextjs/pages/guides/incremental-static-regeneration', label: 'ISR', translations: { en: 'ISR' } },
			{ slug: 'nextjs/pages/guides/instrumentation', label: '계측', translations: { en: 'Instrumentation' } },
			{ slug: 'nextjs/pages/guides/internationalization', label: '국제화', translations: { en: 'Internationalization' } },
			{ slug: 'nextjs/pages/guides/lazy-loading', label: '지연 로딩', translations: { en: 'Lazy Loading' } },
			{ slug: 'nextjs/pages/guides/mdx', label: 'MDX', translations: { en: 'MDX' } },
			{
				label: '마이그레이션',
				translations: { en: 'Migrating' },
				items: [
				{ slug: 'nextjs/pages/guides/migrating', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/guides/migrating/app-router-migration', label: 'App Router', translations: { en: 'App Router' } },
				{ slug: 'nextjs/pages/guides/migrating/from-create-react-app', label: 'Create React App', translations: { en: 'Create React App' } },
				{ slug: 'nextjs/pages/guides/migrating/from-vite', label: 'Vite', translations: { en: 'Vite' } }
				],
			},
			{ slug: 'nextjs/pages/guides/multi-zones', label: '멀티 존', translations: { en: 'Multi-Zones' } },
			{ slug: 'nextjs/pages/guides/open-telemetry', label: 'OpenTelemetry', translations: { en: 'OpenTelemetry' } },
			{ slug: 'nextjs/pages/guides/package-bundling', label: '패키지 번들링', translations: { en: 'Package Bundling' } },
			{ slug: 'nextjs/pages/guides/post-css', label: 'PostCSS', translations: { en: 'PostCSS' } },
			{ slug: 'nextjs/pages/guides/preview-mode', label: '미리보기 모드', translations: { en: 'Preview Mode' } },
			{ slug: 'nextjs/pages/guides/production-checklist', label: '프로덕션', translations: { en: 'Production' } },
			{ slug: 'nextjs/pages/guides/redirecting', label: '리다이렉트', translations: { en: 'Redirecting' } },
			{ slug: 'nextjs/pages/guides/sass', label: 'Sass', translations: { en: 'Sass' } },
			{ slug: 'nextjs/pages/guides/scripts', label: '스크립트', translations: { en: 'Scripts' } },
			{ slug: 'nextjs/pages/guides/self-hosting', label: '셀프 호스팅', translations: { en: 'Self-Hosting' } },
			{ slug: 'nextjs/pages/guides/static-exports', label: '정적 내보내기', translations: { en: 'Static Exports' } },
			{ slug: 'nextjs/pages/guides/tailwind-v3-css', label: 'Tailwind CSS', translations: { en: 'Tailwind CSS' } },
			{
				label: '테스팅',
				translations: { en: 'Testing' },
				items: [
				{ slug: 'nextjs/pages/guides/testing', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/guides/testing/cypress', label: 'Cypress', translations: { en: 'Cypress' } },
				{ slug: 'nextjs/pages/guides/testing/jest', label: 'Jest', translations: { en: 'Jest' } },
				{ slug: 'nextjs/pages/guides/testing/playwright', label: 'Playwright', translations: { en: 'Playwright' } },
				{ slug: 'nextjs/pages/guides/testing/vitest', label: 'Vitest', translations: { en: 'Vitest' } }
				],
			},
			{ slug: 'nextjs/pages/guides/third-party-libraries', label: '서드파티 라이브러리', translations: { en: 'Third Party Libraries' } },
			{
				label: '업그레이드',
				translations: { en: 'Upgrading' },
				items: [
				{ slug: 'nextjs/pages/guides/upgrading', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/guides/upgrading/codemods', label: 'Codemods', translations: { en: 'Codemods' } },
				{ slug: 'nextjs/pages/guides/upgrading/version-10', label: '버전 10', translations: { en: 'Version 10' } },
				{ slug: 'nextjs/pages/guides/upgrading/version-11', label: '버전 11', translations: { en: 'Version 11' } },
				{ slug: 'nextjs/pages/guides/upgrading/version-12', label: '버전 12', translations: { en: 'Version 12' } },
				{ slug: 'nextjs/pages/guides/upgrading/version-13', label: '버전 13', translations: { en: 'Version 13' } },
				{ slug: 'nextjs/pages/guides/upgrading/version-14', label: '버전 14', translations: { en: 'Version 14' } },
				{ slug: 'nextjs/pages/guides/upgrading/version-9', label: '버전 9', translations: { en: 'Version 9' } }
				],
			}
			],
		},
		{
			label: '애플리케이션 구축',
			translations: { en: 'Building Your Application' },
			items: [
			{ slug: 'nextjs/pages/building-your-application', label: '개요', translations: { en: 'Overview' } },
			{
				label: '라우팅',
				translations: { en: 'Routing' },
				items: [
				{ slug: 'nextjs/pages/building-your-application/routing', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/building-your-application/routing/pages-and-layouts', label: '페이지와 레이아웃', translations: { en: 'Pages and Layouts' } },
				{ slug: 'nextjs/pages/building-your-application/routing/dynamic-routes', label: '동적 라우트', translations: { en: 'Dynamic Routes' } },
				{ slug: 'nextjs/pages/building-your-application/routing/linking-and-navigating', label: '링크 및 탐색', translations: { en: 'Linking and Navigating' } },
				{ slug: 'nextjs/pages/building-your-application/routing/custom-app', label: '커스텀 App', translations: { en: 'Custom App' } },
				{ slug: 'nextjs/pages/building-your-application/routing/custom-document', label: '커스텀 Document', translations: { en: 'Custom Document' } },
				{ slug: 'nextjs/pages/building-your-application/routing/api-routes', label: 'API 라우트', translations: { en: 'API Routes' } },
				{ slug: 'nextjs/pages/building-your-application/routing/custom-error', label: '커스텀 오류', translations: { en: 'Custom Errors' } }
				],
			},
			{
				label: '렌더링',
				translations: { en: 'Rendering' },
				items: [
				{ slug: 'nextjs/pages/building-your-application/rendering/server-side-rendering', label: '서버사이드 렌더링 (SSR)', translations: { en: 'Server-side Rendering (SSR)' } },
				{ slug: 'nextjs/pages/building-your-application/rendering/static-site-generation', label: '정적 사이트 생성 (SSG)', translations: { en: 'Static Site Generation (SSG)' } },
				{ slug: 'nextjs/pages/building-your-application/rendering/automatic-static-optimization', label: '자동 정적 최적화', translations: { en: 'Automatic Static Optimization' } },
				{ slug: 'nextjs/pages/building-your-application/rendering/client-side-rendering', label: '클라이언트사이드 렌더링 (CSR)', translations: { en: 'Client-side Rendering (CSR)' } }
				],
			},
			{
				label: '데이터 가져오기',
				translations: { en: 'Data Fetching' },
				items: [
				{ slug: 'nextjs/pages/building-your-application/data-fetching', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/building-your-application/data-fetching/get-static-props', label: 'getStaticProps', translations: { en: 'getStaticProps' } },
				{ slug: 'nextjs/pages/building-your-application/data-fetching/get-static-paths', label: 'getStaticPaths', translations: { en: 'getStaticPaths' } },
				{ slug: 'nextjs/pages/building-your-application/data-fetching/get-server-side-props', label: 'getServerSideProps', translations: { en: 'getServerSideProps' } },
				{ slug: 'nextjs/pages/building-your-application/data-fetching/client-side', label: '클라이언트사이드 가져오기', translations: { en: 'Client-side Fetching' } }
				],
			},
			{
				label: '구성',
				translations: { en: 'Configuring' },
				items: [
				{ slug: 'nextjs/pages/building-your-application/configuring', label: '개요', translations: { en: 'Overview' } }
				],
			}
			],
		},
		{
			label: 'API 참조',
			translations: { en: 'API Reference' },
			items: [
			{ slug: 'nextjs/pages/api-reference', label: '개요', translations: { en: 'Overview' } },
			{
				label: '컴포넌트',
				translations: { en: 'Components' },
				items: [
				{ slug: 'nextjs/pages/api-reference/components', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/api-reference/components/font', label: '폰트', translations: { en: 'Font' } },
				{ slug: 'nextjs/pages/api-reference/components/form', label: '폼', translations: { en: 'Form' } },
				{ slug: 'nextjs/pages/api-reference/components/head', label: 'Head', translations: { en: 'Head' } },
				{ slug: 'nextjs/pages/api-reference/components/image', label: '이미지', translations: { en: 'Image' } },
				{ slug: 'nextjs/pages/api-reference/components/image-legacy', label: '이미지 (레거시)', translations: { en: 'Image (Legacy)' } },
				{ slug: 'nextjs/pages/api-reference/components/link', label: '링크', translations: { en: 'Link' } },
				{ slug: 'nextjs/pages/api-reference/components/script', label: '스크립트', translations: { en: 'Script' } }
				],
			},
			{
				label: '파일 시스템 컨벤션',
				translations: { en: 'File-system conventions' },
				items: [
				{ slug: 'nextjs/pages/api-reference/file-conventions', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/api-reference/file-conventions/instrumentation', label: 'instrumentation.js', translations: { en: 'instrumentation.js' } },
				{ slug: 'nextjs/pages/api-reference/file-conventions/proxy', label: '프록시', translations: { en: 'Proxy' } },
				{ slug: 'nextjs/pages/api-reference/file-conventions/public-folder', label: 'public', translations: { en: 'public' } },
				{ slug: 'nextjs/pages/api-reference/file-conventions/src-folder', label: 'src 디렉토리', translations: { en: 'src Directory' } }
				],
			},
			{
				label: '함수',
				translations: { en: 'Functions' },
				items: [
				{ slug: 'nextjs/pages/api-reference/functions', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/api-reference/functions/get-initial-props', label: 'getInitialProps', translations: { en: 'getInitialProps' } },
				{ slug: 'nextjs/pages/api-reference/functions/get-server-side-props', label: 'getServerSideProps', translations: { en: 'getServerSideProps' } },
				{ slug: 'nextjs/pages/api-reference/functions/get-static-paths', label: 'getStaticPaths', translations: { en: 'getStaticPaths' } },
				{ slug: 'nextjs/pages/api-reference/functions/get-static-props', label: 'getStaticProps', translations: { en: 'getStaticProps' } },
				{ slug: 'nextjs/pages/api-reference/functions/next-request', label: 'NextRequest', translations: { en: 'NextRequest' } },
				{ slug: 'nextjs/pages/api-reference/functions/next-response', label: 'NextResponse', translations: { en: 'NextResponse' } },
				{ slug: 'nextjs/pages/api-reference/functions/use-params', label: 'useParams', translations: { en: 'useParams' } },
				{ slug: 'nextjs/pages/api-reference/functions/use-report-web-vitals', label: 'useReportWebVitals', translations: { en: 'useReportWebVitals' } },
				{ slug: 'nextjs/pages/api-reference/functions/use-router', label: 'useRouter', translations: { en: 'useRouter' } },
				{ slug: 'nextjs/pages/api-reference/functions/use-search-params', label: 'useSearchParams', translations: { en: 'useSearchParams' } },
				{ slug: 'nextjs/pages/api-reference/functions/userAgent', label: 'userAgent', translations: { en: 'userAgent' } }
				],
			},
			{
				label: '구성',
				translations: { en: 'Configuration' },
				items: [
				{ slug: 'nextjs/pages/api-reference/config', label: '개요', translations: { en: 'Overview' } },
				{
					label: 'next.config.js 옵션',
					translations: { en: 'next.config.js Options' },
					items: [
					{ slug: 'nextjs/pages/api-reference/config/next-config-js', label: '개요', translations: { en: 'Overview' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/adapterPath', label: 'experimental.adapterPath', translations: { en: 'experimental.adapterPath' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/allowedDevOrigins', label: 'allowedDevOrigins', translations: { en: 'allowedDevOrigins' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/assetPrefix', label: 'assetPrefix', translations: { en: 'assetPrefix' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/basePath', label: 'basePath', translations: { en: 'basePath' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/bundlePagesRouterDependencies', label: 'bundlePagesRouterDependencies', translations: { en: 'bundlePagesRouterDependencies' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/compress', label: 'compress', translations: { en: 'compress' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/crossOrigin', label: 'crossOrigin', translations: { en: 'crossOrigin' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/deploymentId', label: 'deploymentId', translations: { en: 'deploymentId' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/devIndicators', label: 'devIndicators', translations: { en: 'devIndicators' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/distDir', label: 'distDir', translations: { en: 'distDir' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/env', label: 'env', translations: { en: 'env' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/exportPathMap', label: 'exportPathMap', translations: { en: 'exportPathMap' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/generateBuildId', label: 'generateBuildId', translations: { en: 'generateBuildId' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/generateEtags', label: 'generateEtags', translations: { en: 'generateEtags' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/headers', label: 'headers', translations: { en: 'headers' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/httpAgentOptions', label: 'httpAgentOptions', translations: { en: 'httpAgentOptions' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/images', label: 'images', translations: { en: 'images' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/isolatedDevBuild', label: 'isolatedDevBuild', translations: { en: 'isolatedDevBuild' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/onDemandEntries', label: 'onDemandEntries', translations: { en: 'onDemandEntries' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/optimizePackageImports', label: 'optimizePackageImports', translations: { en: 'optimizePackageImports' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/output', label: 'output', translations: { en: 'output' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/pageExtensions', label: 'pageExtensions', translations: { en: 'pageExtensions' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/poweredByHeader', label: 'poweredByHeader', translations: { en: 'poweredByHeader' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/productionBrowserSourceMaps', label: 'productionBrowserSourceMaps', translations: { en: 'productionBrowserSourceMaps' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/proxyClientMaxBodySize', label: 'experimental.proxyClientMaxBodySize', translations: { en: 'experimental.proxyClientMaxBodySize' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/reactStrictMode', label: 'reactStrictMode', translations: { en: 'reactStrictMode' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/redirects', label: 'redirects', translations: { en: 'redirects' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/rewrites', label: 'rewrites', translations: { en: 'rewrites' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/serverExternalPackages', label: 'serverExternalPackages', translations: { en: 'serverExternalPackages' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/trailingSlash', label: 'trailingSlash', translations: { en: 'trailingSlash' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/transpilePackages', label: 'transpilePackages', translations: { en: 'transpilePackages' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/turbopack', label: 'turbopack', translations: { en: 'turbopack' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/typescript', label: 'typescript', translations: { en: 'typescript' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/urlImports', label: 'urlImports', translations: { en: 'urlImports' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/useLightningcss', label: 'useLightningcss', translations: { en: 'useLightningcss' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/webpack', label: 'webpack', translations: { en: 'webpack' } },
					{ slug: 'nextjs/pages/api-reference/config/next-config-js/webVitalsAttribution', label: 'webVitalsAttribution', translations: { en: 'webVitalsAttribution' } }
					],
				},
				{ slug: 'nextjs/pages/api-reference/config/typescript', label: 'TypeScript', translations: { en: 'TypeScript' } },
				{ slug: 'nextjs/pages/api-reference/config/eslint', label: 'ESLint', translations: { en: 'ESLint' } }
				],
			},
			{
				label: 'CLI',
				translations: { en: 'CLI' },
				items: [
				{ slug: 'nextjs/pages/api-reference/cli', label: '개요', translations: { en: 'Overview' } },
				{ slug: 'nextjs/pages/api-reference/cli/create-next-app', label: 'create-next-app CLI', translations: { en: 'create-next-app CLI' } },
				{ slug: 'nextjs/pages/api-reference/cli/next', label: 'next CLI', translations: { en: 'next CLI' } }
				],
			},
			{ slug: 'nextjs/pages/api-reference/edge', label: 'Edge Runtime', translations: { en: 'Edge Runtime' } },
			{ slug: 'nextjs/pages/api-reference/turbopack', label: 'Turbopack', translations: { en: 'Turbopack' } }
			],
		}
	],
	},
	{
		label: '아키텍처',
		translations: { en: 'Architecture' },
		items: [
		{ slug: 'nextjs/architecture', label: '개요', translations: { en: 'Overview' } },
		{ slug: 'nextjs/architecture/accessibility', label: '접근성', translations: { en: 'Accessibility' } },
		{ slug: 'nextjs/architecture/fast-refresh', label: '빠른 새로 고침', translations: { en: 'Fast Refresh' } },
		{ slug: 'nextjs/architecture/nextjs-compiler', label: 'Next.js 컴파일러', translations: { en: 'Next.js Compiler' } },
		{ slug: 'nextjs/architecture/supported-browsers', label: '지원 브라우저', translations: { en: 'Supported Browsers' } }
		],
	},
	{
		label: '커뮤니티',
		translations: { en: 'Community' },
		items: [
		{ slug: 'nextjs/community', label: '개요', translations: { en: 'Overview' } },
		{ slug: 'nextjs/community/contribution-guide', label: '기여 가이드', translations: { en: 'Contribution Guide' } },
		{ slug: 'nextjs/community/rspack', label: 'Rspack', translations: { en: 'Rspack' } }
		],
	},
],
			},
			
{
	label: 'Zod',
	translations: { en: 'Zod' },
	items: [
		{ slug: 'zod', label: 'Overview', translations: { en: 'Overview' } },
		{ slug: 'zod/api', label: 'Api', translations: { en: 'Api' } },
		{ slug: 'zod/basics', label: 'Basics', translations: { en: 'Basics' } },
		{ slug: 'zod/codecs', label: 'Codecs', translations: { en: 'Codecs' } },
		{ slug: 'zod/ecosystem', label: 'Ecosystem', translations: { en: 'Ecosystem' } },
		{ slug: 'zod/error-customization', label: 'Error Customization', translations: { en: 'Error Customization' } },
		{ slug: 'zod/error-formatting', label: 'Error Formatting', translations: { en: 'Error Formatting' } },
		{ slug: 'zod/json-schema', label: 'Json Schema', translations: { en: 'Json Schema' } },
		{ slug: 'zod/library-authors', label: 'Library Authors', translations: { en: 'Library Authors' } },
		{ slug: 'zod/llms.txt', label: 'Llms.Txt', translations: { en: 'Llms.Txt' } },
		{ slug: 'zod/metadata', label: 'Metadata', translations: { en: 'Metadata' } },
		{
			label: 'Packages',
			translations: { en: 'Packages' },
			items: [
			{ slug: 'zod/packages/core', label: 'Core', translations: { en: 'Core' } },
			{ slug: 'zod/packages/mini', label: 'Mini', translations: { en: 'Mini' } },
			{ slug: 'zod/packages/zod', label: 'Zod', translations: { en: 'Zod' } }
			],
		},
		{
			label: 'V4',
			translations: { en: 'V4' },
			items: [
			{ slug: 'zod/v4', label: 'Overview', translations: { en: 'Overview' } },
			{ slug: 'zod/v4/changelog', label: 'Changelog', translations: { en: 'Changelog' } }
			],
		}
	],
},
			
];
