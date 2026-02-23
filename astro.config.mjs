import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
	site: 'https://dev-docs.moodybeard.com',
	integrations: [
		starlight({
			title: 'dev-docs',
			components: {
				Head: './src/components/Head.astro',
			},
			head: [
				{
					tag: 'script',
					attrs: { type: 'application/ld+json' },
					content: JSON.stringify({
						'@context': 'https://schema.org',
						'@type': 'WebSite',
						name: 'dev-docs',
						url: 'https://dev-docs.moodybeard.com',
					}),
				},
			],
			locales: {
				root: { label: '한국어', lang: 'ko' },
				en: { label: 'English', lang: 'en' },
			},
			sidebar: [
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
					autogenerate: { directory: 'nextjs' },
				},
			],
		}),
		sitemap(),
	],
});
